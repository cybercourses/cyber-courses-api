#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tiny API server for the courses app (no secrets here).

Endpoints (all JSON):
    GET  /health                         -> {"ok": true, "hosted": false}
    GET  /lessons
        All 176 FREE lessons, in the exact same JSON shape as the
        bundled assets/lessons.json (17 tracks). Built fresh from
        bot/lessons.py, so new lessons appear here as soon as the
        content file is updated — the app fetches this when online and
        caches it, so new content needs NO new APK. The special (paid)
        course is NEVER in this response.
    POST /verify-code   {"code": "123456"}
        Verifies a one-time 6-digit login code issued by the Telegram bot
        (/login). A code works exactly once and expires after 10 minutes.
        On success returns the Telegram user id + name so the app can
        store the session locally.
        Rate-limited: max 10 failed attempts per IP per 10 minutes.
    GET  /subscription?telegram_id=123  -> {"subscribed": false, ...}
        Reads the real subscriptions written by the USDT watcher
        (payment-watcher/subscriptions.json): the owner is always
        subscribed, anyone else needs a live 30-day subscription.
    GET  /special-lessons?telegram_id=123
        Returns the SPECIAL (paid) course lessons ONLY when the Telegram
        user is a subscriber. Otherwise 403 {"subscribed": false}.
        The paid lessons are NOT bundled in the APK — they only ever come
        from this server after the subscription check passes.
    GET  /payment-info
        What the in-app Subscribe screen shows: price ($5/month), payment
        by Binance USDT, and the payment instructions. The USDT address
        is read live from the watcher config — it is null until Khaled
        provides it (never invented). The unique-amount assignment +
        on-chain watcher (auto-unlock on payment) is wired: the bot
        assigns amounts, the watcher credits on-chain, the bot sends
        "تم الدفع ✅" + the first special lesson.

Hosted mode (PythonAnywhere, free hosting):
    Set env API_HOSTED_MODE=1. The hosted server cannot read this VM's
    files, so it keeps its OWN persistent stores next to this file:
      hosted_login_codes.json   (codes pushed by the bot)
      hosted_subscriptions.json (subscriptions pushed by the watcher)
      hosted_payment_info.json  (optional USDT address, pushed too)
    /verify-code, /subscription and /special-lessons then read those
    stores instead of the local files. Local mode (the default, no env
    set) behaves EXACTLY as before: bot/login_codes.json +
    payments.check_subscription. Nothing breaks if the push endpoints
    below are never called.
    POST /internal/login-code    {"code", "user_id", "name", "username",
                                 "expires"}  (header X-Internal-Secret)
    POST /internal/subscriptions {"telegram_id", "subscribed_until"}
                                 (header X-Internal-Secret; optional
                                  "usdt_address" is stored for
                                  /payment-info)
    Both require the shared secret (env INTERNAL_SECRET, the same value
    the bot/watcher use). In hosted mode the secret MUST be set to a
    real value; in local mode the dev value "dev-internal-secret" is
    accepted for local testing only. No secret is ever logged.

Run:  python3 app.py   (listens on 0.0.0.0:5000)
Service: cyber-courses-api.service (systemd, Restart=always).
"""

import json
import os
import sys
import time

from flask import Flask, jsonify, request

# Payment watcher (USDT unique amounts): guarded import so the server
# still runs if the watcher folder is ever missing — subscription checks
# then fall back to owner-only.
try:
    sys.path.insert(
        0,
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "..", "..", "payment-watcher")),
    )
    import payments as _payments
except Exception:  # pragma: no cover - watcher folder missing
    _payments = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "bot"))
LOGIN_CODES_PATH = os.path.join(BOT_DIR, "login_codes.json")

# Hosted-mode stores (live next to this file; only used when
# API_HOSTED_MODE=1, and only written by the /internal/* endpoints).
HOSTED_LOGIN_CODES_PATH = os.path.join(BASE_DIR, "hosted_login_codes.json")
HOSTED_SUBSCRIPTIONS_PATH = os.path.join(BASE_DIR, "hosted_subscriptions.json")
HOSTED_PAYMENT_INFO_PATH = os.path.join(BASE_DIR, "hosted_payment_info.json")

# Dev-only internal secret, accepted ONLY in local mode for testing.
# In hosted mode a real INTERNAL_SECRET must be set (see _internal_auth).
DEV_INTERNAL_SECRET = "dev-internal-secret"

LOGIN_CODE_TTL = 600  # seconds (10 minutes); each code works exactly once.

# --- brute-force guard for /verify-code: 10 failed tries per IP / 10 min ---
ATTEMPT_LIMIT = 10
ATTEMPT_WINDOW = 600  # seconds
_failed_attempts = {}  # ip -> [window_start, count]


def _hosted_mode():
    """True when this server runs hosted (PythonAnywhere), away from
    the bot/watcher files. Read dynamically so tests can toggle it."""
    return os.environ.get("API_HOSTED_MODE") == "1"


def _rate_limited(ip):
    now = time.time()
    entry = _failed_attempts.get(ip)
    if entry is None or now - entry[0] > ATTEMPT_WINDOW:
        _failed_attempts[ip] = [now, 0]
        return False
    return entry[1] >= ATTEMPT_LIMIT


def _record_failure(ip):
    now = time.time()
    entry = _failed_attempts.get(ip)
    if entry is None or now - entry[0] > ATTEMPT_WINDOW:
        _failed_attempts[ip] = [now, 1]
    else:
        entry[1] += 1


# ------------------------------------------------------------ JSON stores
def _load_json_file(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, type(default)) else default
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def _save_json_atomic(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    os.replace(tmp, path)


def _load_login_codes():
    return _load_json_file(LOGIN_CODES_PATH, {})


def _save_login_codes(codes):
    _save_json_atomic(LOGIN_CODES_PATH, codes)


def _load_hosted_login_codes():
    return _load_json_file(HOSTED_LOGIN_CODES_PATH, {})


def _save_hosted_login_codes(codes):
    _save_json_atomic(HOSTED_LOGIN_CODES_PATH, codes)


def _load_hosted_subscriptions():
    return _load_json_file(HOSTED_SUBSCRIPTIONS_PATH, {})


def _save_hosted_subscriptions(subs):
    _save_json_atomic(HOSTED_SUBSCRIPTIONS_PATH, subs)


def _load_hosted_payment_info():
    return _load_json_file(HOSTED_PAYMENT_INFO_PATH, {})


def _save_hosted_payment_info(info):
    _save_json_atomic(HOSTED_PAYMENT_INFO_PATH, info)


def _prune_login_codes(codes, now):
    """Drop expired / already-used codes so the store never grows."""
    return {
        c: v for c, v in codes.items()
        if v.get("expires", 0) > now and not v.get("used")
    }


# ------------------------------------------------------- internal auth
def _internal_auth():
    """Check the X-Internal-Secret header. Returns (ok, reason).

    Hosted mode: INTERNAL_SECRET must be set to a real (non-dev) value.
    Local mode: the env value, or the dev secret, is accepted (testing).
    The secret value itself is never logged or returned.
    """
    provided = request.headers.get("X-Internal-Secret", "")
    configured = (os.environ.get("INTERNAL_SECRET") or "").strip()
    if _hosted_mode():
        if not configured or configured == DEV_INTERNAL_SECRET:
            return False, "not_configured"
        return provided == configured, "bad_secret"
    expected = configured or DEV_INTERNAL_SECRET
    return provided == expected, "bad_secret"


OWNER_TELEGRAM_ID = "1817814526"  # Khaled (@Telecom_Service) — the owner.


def is_subscribed(telegram_id):
    """Is this Telegram user a subscriber of the special course?

    The OWNER is always subscribed (admin): he tests the special course
    in the app after logging in. Everyone else needs a live subscription:
    in local mode the USDT watcher's subscriptions.json (via
    payments.check_subscription); in hosted mode the hosted store that
    the watcher pushes to.
    """
    if str(telegram_id).strip() == OWNER_TELEGRAM_ID:
        return True
    if _hosted_mode():
        subs = _load_hosted_subscriptions()
        entry = subs.get(str(telegram_id))
        if not entry:
            return False
        return entry.get("expires_at", 0) > time.time()
    if _payments is not None:
        try:
            return _payments.check_subscription(telegram_id)
        except Exception:
            pass
    return str(telegram_id).strip() == OWNER_TELEGRAM_ID


# ------------------------------------------------------------ free lessons
_lessons_payload = None
_lessons_mtime = None


def _free_lessons_payload():
    """The free-lessons payload, rebuilt when bot/lessons.py changes.

    Same shape as the bundled assets/lessons.json (see
    bot/lessons_export.py). Cached in memory; reloaded only when the
    content file's mtime moves, so new lessons appear without a server
    restart.
    """
    global _lessons_payload, _lessons_mtime
    lessons_path = os.path.join(BOT_DIR, "lessons.py")
    try:
        mtime = os.path.getmtime(lessons_path)
    except OSError:
        mtime = None
    if _lessons_payload is None or mtime != _lessons_mtime:
        sys.path.insert(0, BOT_DIR)
        from lessons_export import build_tracks_payload

        _lessons_payload = build_tracks_payload()
        _lessons_mtime = mtime
    return _lessons_payload


app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"ok": True, "hosted": _hosted_mode()})


@app.get("/lessons")
def lessons():
    """All free lessons (same shape as the bundled asset)."""
    try:
        return jsonify(_free_lessons_payload())
    except AssertionError as exc:
        return jsonify({"ok": False, "error": "bad_content", "detail": str(exc)}), 500


@app.post("/verify-code")
def verify_code():
    ip = request.remote_addr or "unknown"
    if _rate_limited(ip):
        return jsonify({"ok": False, "error": "too_many_attempts"}), 429
    body = request.get_json(silent=True) or {}
    code = str(body.get("code", "")).strip()
    if len(code) != 6 or not code.isdigit():
        _record_failure(ip)
        return jsonify({"ok": False, "error": "invalid_code"}), 400
    now = time.time()
    if _hosted_mode():
        codes = _prune_login_codes(_load_hosted_login_codes(), now)
        entry = codes.get(code)
        if (
            entry is None
            or entry.get("used")
            or entry.get("expires", 0) <= now
        ):
            _record_failure(ip)
            return jsonify({"ok": False, "error": "invalid_or_expired"}), 400
        entry["used"] = True
        codes[code] = entry
        _save_hosted_login_codes(codes)
    else:
        codes = _load_login_codes()
        entry = codes.get(code)
        if (
            entry is None
            or entry.get("used")
            or entry.get("expires", 0) <= now
        ):
            _record_failure(ip)
            return jsonify({"ok": False, "error": "invalid_or_expired"}), 400
        # Single use: mark used before replying.
        entry["used"] = True
        codes[code] = entry
        _save_login_codes(codes)
    return jsonify(
        {
            "ok": True,
            "telegram_id": entry.get("user_id"),
            "name": entry.get("name", ""),
            "username": entry.get("username"),
        }
    )


@app.post("/internal/login-code")
def internal_login_code():
    """Store a login code the bot just issued (hosted API only).

    Body: {"code", "user_id", "name", "username", "expires"}.
    "expires" is optional (defaults to now + 10 minutes). Same format
    and one-time semantics as bot/login_codes.json.
    """
    ok, reason = _internal_auth()
    if not ok:
        status = 503 if reason == "not_configured" else 401
        return jsonify({"ok": False, "error": reason}), status
    body = request.get_json(silent=True) or {}
    code = str(body.get("code", "")).strip()
    if len(code) != 6 or not code.isdigit():
        return jsonify({"ok": False, "error": "invalid_code"}), 400
    now = time.time()
    try:
        expires = float(body.get("expires") or 0)
    except (TypeError, ValueError):
        expires = 0
    if expires <= now:
        expires = now + LOGIN_CODE_TTL
    codes = _prune_login_codes(_load_hosted_login_codes(), now)
    codes[code] = {
        "user_id": body.get("user_id"),
        "name": body.get("name", ""),
        "username": body.get("username"),
        "created": now,
        "expires": expires,
        "used": False,
    }
    _save_hosted_login_codes(codes)
    return jsonify({"ok": True, "stored": True})


@app.post("/internal/subscriptions")
def internal_subscriptions():
    """Store a created/renewed subscription (hosted API only).

    Body: {"telegram_id", "subscribed_until"} (epoch seconds; the key
    "expires_at" is accepted as an alias). An optional "usdt_address"
    is stored for /payment-info. The hosted /subscription and
    /special-lessons endpoints read this store.
    """
    ok, reason = _internal_auth()
    if not ok:
        status = 503 if reason == "not_configured" else 401
        return jsonify({"ok": False, "error": reason}), status
    body = request.get_json(silent=True) or {}
    telegram_id = str(body.get("telegram_id", "")).strip()
    try:
        expires_at = float(
            body.get("subscribed_until", body.get("expires_at", 0)) or 0
        )
    except (TypeError, ValueError):
        expires_at = 0
    address = str(body.get("usdt_address") or "").strip()
    if address:
        _save_hosted_payment_info({"usdt_address": address})
    if not telegram_id or expires_at <= 0:
        # An address-only call is fine (nothing else to store).
        if address:
            return jsonify({"ok": True, "stored": "usdt_address"})
        return jsonify({"ok": False, "error": "bad_subscription"}), 400
    subs = _load_hosted_subscriptions()
    subs[telegram_id] = {
        "user_id": telegram_id,
        "expires_at": expires_at,
        "updated_at": time.time(),
    }
    _save_hosted_subscriptions(subs)
    return jsonify({"ok": True, "stored": True})


@app.get("/subscription")
def subscription():
    telegram_id = request.args.get("telegram_id", "")
    return jsonify(
        {"ok": True, "telegram_id": telegram_id, "subscribed": is_subscribed(telegram_id)}
    )


# Payment details for the in-app Subscribe screen. The price/method are
# fixed (decided: $5/month, Binance USDT). The actual destination —
# Khaled's Binance Pay ID / USDT address — is NOT known to this server
# yet, so those fields are null until he provides them; nothing is
# invented here. The usdt_address is read live from the watcher config
# on every /payment-info request (local mode), or from the hosted store
# (hosted mode), so it appears in the app as soon as Khaled's address
# is added (no server restart needed).
PAYMENT_INFO = {
    "ok": True,
    "price_usd": 5,
    "currency": "USDT",
    "period": "monthly",
    "period_ar": "في الشهر",
    "method": "binance",
    "method_ar": "بينانس (Binance)",
    "pay_id": None,
    "usdt_address": None,
    "note_ar": (
        "ادفع 5 دولار (USDT) من حسابك على بينانس، وبعد ما نتأكد من وصول "
        "الدفع هتتفتح لك الدورة الخاصة لمدة 30 يوم. عنوان الدفع هيظهر هنا "
        "أول ما يتضاف."
    ),
    "note_en": (
        "Pay 5 USDT from your Binance account. Once the payment is "
        "confirmed, the special course unlocks for 30 days. The payment "
        "address will appear here once it is added."
    ),
    "steps_ar": [
        "افتح تطبيق بينانس على موبايلك.",
        "ابعت 5 USDT (بينانس لبينانس) لعنوان الدفع اللي هيظهر هنا.",
        "بعد ما نتأكد من وصول الدفع، الدورة الخاصة هتتفتح لك لمدة 30 يوم.",
        "لو دفعت خلاص ولسه الدورة مقفولة، دوس على زرار «تأكد من الاشتراك» تحت.",
    ],
    "steps_en": [
        "Open the Binance app on your phone.",
        "Send 5 USDT (Binance to Binance) to the payment address shown here.",
        "Once the payment is confirmed, the special course unlocks for 30 days.",
        "If you already paid and the course is still locked, tap “Check subscription” below.",
    ],
}


@app.get("/payment-info")
def payment_info():
    info = dict(PAYMENT_INFO)
    try:
        if _hosted_mode():
            address = (_load_hosted_payment_info().get("usdt_address") or "").strip()
            info["usdt_address"] = address or None
        elif _payments is not None:
            address = (_payments.load_config().get("usdt_address") or "").strip()
            info["usdt_address"] = address or None
    except Exception:
        pass
    return jsonify(info)


@app.get("/special-lessons")
def special_lessons():
    telegram_id = request.args.get("telegram_id", "")
    if not is_subscribed(telegram_id):
        return (
            jsonify(
                {
                    "ok": False,
                    "subscribed": False,
                    "error": "not_subscribed",
                    "message": "الدورة الخاصة للمشتركين بس — الاشتراكات لسه ما اتفتحتش.",
                }
            ),
            403,
        )
    sys.path.insert(0, BOT_DIR)
    from special_lessons import SPECIAL_LESSONS

    return jsonify({"ok": True, "subscribed": True, "lessons": SPECIAL_LESSONS})


if __name__ == "__main__":
    # Dev server is fine for now (tiny traffic). If the app grows, run
    # behind waitress/gunicorn instead.
    app.run(host="0.0.0.0", port=5000, threaded=True)
