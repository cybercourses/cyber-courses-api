#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Core payment logic for the Telegram courses USDT watcher.

NO network calls here — only stores + matching rules. The chain polling
lives in watcher.py; this module is what the bot and the app server will
import later (assign_amount / check_subscription / credit_payment).

Payment model (decided by Khaled):
  * Binance USDT, $5/month, special course only.
  * Every subscriber gets a UNIQUE exact amount: $5.00, $5.01, ... $5.99.
    The cents are only an ID tag — the price is always $5.
  * A pending assignment lives 1 hour; after that the amount is free again.
  * When a payment of exactly a pending amount arrives, the user is a
    subscriber for 30 days. No manual step, no screenshot proof.

Pools (so eSIM sales can never be mistaken for course subscriptions):
  * "course" — the $5.00-$5.99 pool above. Default; behaviour unchanged.
  * "esim" — a SEPARATE pool for eSIM sales: whole-dollar price tiers
    ($10, $11, ... $99), each tier getting its own 100 unique amounts
    (tier base .. base+99, e.g. $10.00-$10.99). An eSIM payment is
    recorded in esim_payments.json and NEVER creates a course
    subscription, unlock or reminder. Amounts are unique GLOBALLY
    across pools (one busy set), so a course amount and an eSIM amount
    can never collide even while both are pending.

Safety rules (never bend these):
  * An amount is "busy" while it is pending (not expired) OR while the
    subscription it created is still live. Re-using an amount while its
    subscription is live could credit a renewal payment to the WRONG
    person, so we wait until that subscription expires. (The pool has
    100 amounts and a 1-hour pending window, so this never blocks.)
  * A transfer is credited ONLY when: right token contract, right
    destination address, exact amount in $5.00-$5.99, a live pending
    assignment for that amount exists, enough confirmations, and the
    transaction hash was never credited before (idempotency).
  * No secrets anywhere in this file. The USDT address comes from
    watcher_config.json, which Khaled fills in himself.

Amounts are handled as INTEGER cents everywhere (503 = $5.03) so float
rounding can never mis-match a payment. USDT has 6 decimals on-chain:
$5.03 = 5,030,000 base units.
"""

import json
import os
import sys
import time
from decimal import Decimal, InvalidOperation

# Push new/renewed subscriptions to the HOSTED API (PythonAnywhere)
# when configured, so the hosted app server knows who paid. Guarded
# import: when hosted_sync (or the bot folder) is missing, or no hosted
# URL is configured, the push is a silent no-op and nothing else
# changes — the local subscription still works exactly as today.
try:
    sys.path.insert(
        0,
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "..", "bot")),
    )
    from hosted_sync import push_subscription as _push_subscription
except Exception:  # pragma: no cover - bot folder / hosted_sync missing
    _push_subscription = None

# ---------------------------------------------------------------- constants
ADMIN_TELEGRAM_ID = 1817814526  # Khaled (@Telecom_Service) — always subscribed.

PRICE_CENTS = 500               # $5.00 — the real price.
AMOUNT_MIN_CENTS = 500          # $5.00 — first unique amount.
AMOUNT_MAX_CENTS = 599          # $5.99 — last unique amount (100 amounts).

# Payment pools. "course" is the $5 special-course pool above (unchanged).
# "esim" is the eSIM pool: whole-dollar tiers ($10, $11, ... $99); each
# tier owns 100 unique amounts (base .. base+99). Tiers never overlap
# each other or the course pool, and the busy set is global, so an eSIM
# payment can never be credited as a course subscription (or vice versa).
COURSE_POOL = "course"
ESIM_POOL = "esim"
ESIM_DEFAULT_BASE_CENTS = 1000  # $10.00 — first eSIM price tier.
ESIM_MIN_CENTS = 1000           # $10.00 — lowest eSIM tier base.
ESIM_MAX_CENTS = 9999           # $99.99 — highest eSIM amount.
POOL_NAMES = (COURSE_POOL, ESIM_POOL)
PENDING_TTL_SECONDS = 3600      # 1 hour: a pending amount then frees up.
SUBSCRIPTION_DAYS = 30          # a paid subscription lasts 30 days.
REMINDER_DAYS_BEFORE = 3        # remind 3 days before expiry.
TRON_CONFIRMATIONS = 19         # blocks to wait on TRON before crediting.
BSC_CONFIRMATIONS = 12          # blocks to wait on BSC before crediting.

USDT_TRON_CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
USDT_BSC_CONTRACT = "0x55d398326f99059fF775485246999027B3197955"
USDT_DECIMALS = 6

DEFAULT_DIR = os.path.dirname(os.path.abspath(__file__))


class AmountPoolExhausted(Exception):
    """All 100 unique amounts are busy right now (practically impossible)."""


# ------------------------------------------------------------------ stores
def _load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, type(default)) else default
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def _save_json_atomic(path, data):
    """Atomic write: write a temp file, then rename (never a half file)."""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def load_config(data_dir=DEFAULT_DIR):
    cfg = _load_json(os.path.join(data_dir, "watcher_config.json"), {})
    cfg.setdefault("network", "")
    cfg.setdefault("usdt_address", "")
    cfg.setdefault("bscscan_api_key", "")
    cfg.setdefault("poll_interval_seconds", 180)
    cfg.setdefault("pending_ttl_seconds", PENDING_TTL_SECONDS)
    cfg.setdefault("subscription_days", SUBSCRIPTION_DAYS)
    cfg.setdefault("reminder_days_before_expiry", REMINDER_DAYS_BEFORE)
    cfg.setdefault("tron_confirmations", TRON_CONFIRMATIONS)
    cfg.setdefault("bsc_confirmations", BSC_CONFIRMATIONS)
    cfg.setdefault("price_usd", 5)
    return cfg


def _pending_path(data_dir):
    return os.path.join(data_dir, "pending.json")


def _subs_path(data_dir):
    return os.path.join(data_dir, "subscriptions.json")


def _unlocks_path(data_dir):
    return os.path.join(data_dir, "unlocks.json")


def _reminders_path(data_dir):
    return os.path.join(data_dir, "reminders.json")


def _esim_payments_path(data_dir):
    return os.path.join(data_dir, "esim_payments.json")


def _state_path(data_dir):
    return os.path.join(data_dir, "watcher_state.json")


def load_pending(data_dir=DEFAULT_DIR):
    return _load_json(_pending_path(data_dir), {})


def load_subscriptions(data_dir=DEFAULT_DIR):
    return _load_json(_subs_path(data_dir), {})


def load_unlocks(data_dir=DEFAULT_DIR):
    return _load_json(_unlocks_path(data_dir), [])


def load_reminders(data_dir=DEFAULT_DIR):
    return _load_json(_reminders_path(data_dir), [])


def load_esim_payments(data_dir=DEFAULT_DIR):
    """Paid eSIM payments waiting for the bot to dispense a code.

    Each entry: {kind: "esim_payment", user_id, amount_cents,
    amount_usd, tx_hash, network, paid_at, delivered: False}.
    The bot's eSIM step drains this list (matches the payment to the
    buyer's pending eSIM order by user_id + amount_cents) and marks
    entries delivered after dispensing. Never creates a subscription.
    """
    return _load_json(_esim_payments_path(data_dir), [])


def load_state(data_dir=DEFAULT_DIR):
    return _load_json(
        _state_path(data_dir),
        {
            "last_tron_block": None,
            "last_bsc_block": None,
            "last_tron_timestamp_ms": None,
            "last_run": None,
            "last_error": None,
            "seen_tx": [],
        },
    )


def save_state(state, data_dir=DEFAULT_DIR):
    _save_json_atomic(_state_path(data_dir), state)


# ------------------------------------------------------------ amount helpers
def cents_to_usd_str(cents):
    """503 -> '5.03' (always two decimals)."""
    return "%.2f" % (cents / 100.0)


def usd_str_to_cents(value):
    """'5.03' / 5.03 / '5' -> 503. Raises ValueError on bad input."""
    try:
        dec = Decimal(str(value).strip())
    except (InvalidOperation, AttributeError):
        raise ValueError("bad amount: %r" % (value,))
    cents = int((dec * 100).to_integral_value())
    if cents < 0:
        raise ValueError("bad amount: %r" % (value,))
    return cents


def base_units_to_cents(value, decimals=USDT_DECIMALS):
    """On-chain base units (e.g. 5030000 for USDT) -> integer cents (503).
    USDT has 6 decimals, so 1 cent = 10^4 base units."""
    return int(value) // (10 ** (decimals - 2))


def cents_to_base_units(cents, decimals=USDT_DECIMALS):
    """503 cents -> 5030000 base units (what the chain actually moves)."""
    return int(cents) * (10 ** (decimals - 2))


def _prune_expired_pending(pending, now):
    return {
        uid: p for uid, p in pending.items() if p.get("expires_at", 0) > now
    }


def _live_subscription_amounts(subs, now):
    return {
        s.get("amount_cents")
        for s in subs.values()
        if s.get("expires_at", 0) > now and s.get("amount_cents") is not None
    }


def _pool_range(pool, base_cents):
    """(low, high) unique-amount range for a pool. Raises ValueError
    on an unknown pool or an invalid eSIM tier base."""
    if pool == COURSE_POOL:
        if base_cents is not None:
            raise ValueError("course pool price is fixed at $5")
        return AMOUNT_MIN_CENTS, AMOUNT_MAX_CENTS
    if pool == ESIM_POOL:
        base = ESIM_DEFAULT_BASE_CENTS if base_cents is None else base_cents
        if (not isinstance(base, int) or base % 100 != 0
                or base < ESIM_MIN_CENTS or base > ESIM_MAX_CENTS - 99):
            raise ValueError(
                "esim base_cents must be a whole-dollar tier "
                "($10-$99, e.g. 1000 for $10, 1500 for $15)"
            )
        return base, base + 99
    raise ValueError("unknown pool: %r (use 'course' or 'esim')" % (pool,))


def _amount_in_known_range(amount):
    """True if this amount could belong to any pool (course $5.00-$5.99
    or an eSIM tier $10.00-$99.99). Anything else is never a payment we
    asked for, so it is rejected before any matching happens."""
    if not isinstance(amount, int):
        return False
    return (AMOUNT_MIN_CENTS <= amount <= AMOUNT_MAX_CENTS
            or ESIM_MIN_CENTS <= amount <= ESIM_MAX_CENTS)


def _pending_key(user_id, pool):
    """Store key for a pending assignment. A user may hold one live
    pending per pool (course + eSIM at the same time), so the key
    includes the pool. Legacy bare user-id keys (written before pools)
    are treated as course-pool entries."""
    return "%s:%s" % (user_id, pool)


# ------------------------------------------------------------- public API
def assign_amount(user_id, data_dir=DEFAULT_DIR, now=None,
                  pool=COURSE_POOL, base_cents=None):
    """Give a user their unique payment amount (integer cents).

    Returns the SAME amount if the user already has a live pending
    assignment in this pool (re-asking /subscribe doesn't burn a new
    amount). Raises AmountPoolExhausted if all amounts in this pool's
    range are busy. Raises ValueError on an unknown pool or a bad
    eSIM tier base.

    pool="course" (default) keeps the exact old behaviour: $5.00-$5.99.
    pool="esim" uses a whole-dollar tier: base_cents=1000 gives
    $10.00-$10.99, 1500 gives $15.00-$15.99, and so on up to $99.
    Amounts are unique GLOBALLY across pools: the busy set covers
    every pending assignment plus every live course subscription, so
    a course amount and an eSIM amount can never be the same.
    """
    low, high = _pool_range(pool, base_cents)
    now = time.time() if now is None else now
    cfg = load_config(data_dir)
    ttl = int(cfg.get("pending_ttl_seconds", PENDING_TTL_SECONDS))
    pending = _prune_expired_pending(load_pending(data_dir), now)
    subs = load_subscriptions(data_dir)

    uid = str(user_id)
    key = _pending_key(uid, pool)
    existing = pending.get(key)
    if existing is None and pool == COURSE_POOL:
        existing = pending.get(uid)  # legacy bare key (pre-pool entry)
    if (existing and existing.get("expires_at", 0) > now
            and existing.get("status", "pending") == "pending"):
        return existing["amount_cents"]

    busy = {p["amount_cents"] for p in pending.values()}
    busy |= _live_subscription_amounts(subs, now)
    for cents in range(low, high + 1):
        if cents not in busy:
            pending[key] = {
                "user_id": int(user_id),
                "pool": pool,
                "base_cents": low,
                "amount_cents": cents,
                "amount_usd": cents_to_usd_str(cents),
                "assigned_at": now,
                "expires_at": now + ttl,
                "status": "pending",
            }
            _save_json_atomic(_pending_path(data_dir), pending)
            return cents
    raise AmountPoolExhausted(
        "all %d unique amounts are busy in the %s pool; try again later"
        % (high - low + 1, pool)
    )


def check_subscription(user_id, data_dir=DEFAULT_DIR, now=None):
    """True if the user may open the special course right now.

    The owner/admin (Khaled) is always subscribed. Anyone else needs a
    live subscription entry (paid_at + 30 days, not expired yet).
    """
    if str(user_id).strip() == str(ADMIN_TELEGRAM_ID):
        return True
    now = time.time() if now is None else now
    subs = load_subscriptions(data_dir)
    entry = subs.get(str(user_id))
    if not entry:
        return False
    return entry.get("expires_at", 0) > now


def subscription_info(user_id, data_dir=DEFAULT_DIR, now=None):
    """The live subscription entry for a user, or None."""
    now = time.time() if now is None else now
    subs = load_subscriptions(data_dir)
    entry = subs.get(str(user_id))
    if entry and entry.get("expires_at", 0) > now:
        return entry
    return None


def credit_payment(transfer, data_dir=DEFAULT_DIR, now=None):
    """Try to credit one on-chain transfer. Returns a result dict.

    transfer = {
      "tx_hash": str, "network": "TRC20" | "BEP20",
      "to": str (destination address), "token": str (contract address),
      "amount_cents": int, "block_number": int,
    }
    The caller (watcher.py) is responsible for the confirmations check
    before calling this — credit_payment only matches + records.

    On a match it records the payment — what it records depends on the
    pool of the pending assignment the amount belongs to:
      * pool "course": the 30-day subscription + unlock event
        (unlocks.json) + reminder event (reminders.json), as before.
      * pool "esim": NO subscription, NO unlock, NO reminder. The
        payment is recorded in esim_payments.json (user_id + amount +
        tx hash) for the bot's eSIM step to dispense a code against the
        buyer's pending eSIM order. An eSIM payment can therefore never
        open the special course, and a course payment can never be
        mistaken for an eSIM purchase.
    """
    now = time.time() if now is None else now
    cfg = load_config(data_dir)
    address = (cfg.get("usdt_address") or "").strip()
    network = str(transfer.get("network", "")).upper()
    tx_hash = str(transfer.get("tx_hash", "")).strip()
    to_addr = str(transfer.get("to", "")).strip()
    token = str(transfer.get("token", "")).strip()
    amount = transfer.get("amount_cents")

    def no_match(reason):
        return {"matched": False, "reason": reason, "tx_hash": tx_hash}

    if not tx_hash:
        return no_match("missing_tx_hash")
    if network not in ("TRC20", "BEP20"):
        return no_match("unknown_network")
    if not address:
        return no_match("no_address_configured")
    if network == "TRC20":
        if to_addr != address:
            return no_match("wrong_address")
        if token != USDT_TRON_CONTRACT:
            return no_match("wrong_token")
    else:  # BEP20 — addresses are case-insensitive (checksummed hex).
        if to_addr.lower() != address.lower():
            return no_match("wrong_address")
        if token.lower() != USDT_BSC_CONTRACT.lower():
            return no_match("wrong_token")
    if not _amount_in_known_range(amount):
        return no_match("wrong_amount")

    state = load_state(data_dir)
    seen = set(state.get("seen_tx") or [])
    if tx_hash in seen:
        return no_match("already_credited")

    pending = _prune_expired_pending(load_pending(data_dir), now)
    owner_uid = None
    owner_entry = None
    for uid, p in pending.items():
        if (p.get("amount_cents") == amount
                and p.get("status", "pending") == "pending"):
            owner_uid = uid
            owner_entry = p
            break
    if owner_uid is None:
        return no_match("no_pending_assignment_for_amount")

    pool = owner_entry.get("pool", COURSE_POOL)

    # ---- match! record everything atomically, one file at a time. ----
    if pool == ESIM_POOL:
        # eSIM payment: mark the pending assignment as paid (it stays
        # busy until its 1-hour expiry, so the amount cannot be
        # recycled to someone else while a double-payment could still
        # arrive), and record the payment for the bot's eSIM step.
        # Deliberately NO subscription, NO unlock, NO reminder.
        owner_entry["status"] = "credited"
        _save_json_atomic(_pending_path(data_dir), pending)

        paid = load_esim_payments(data_dir)
        paid.append(
            {
                "kind": "esim_payment",
                "user_id": int(owner_entry["user_id"]),
                "amount_cents": amount,
                "amount_usd": cents_to_usd_str(amount),
                "paid_at": now,
                "tx_hash": tx_hash,
                "network": network,
                "delivered": False,
                "created_at": now,
            }
        )
        _save_json_atomic(_esim_payments_path(data_dir), paid)

        seen.add(tx_hash)
        state["seen_tx"] = sorted(seen)[-5000:]  # cap: keep the newest 5000.
        save_state(state, data_dir)

        return {
            "matched": True,
            "reason": "credited_esim",
            "pool": ESIM_POOL,
            "tx_hash": tx_hash,
            "user_id": int(owner_entry["user_id"]),
            "amount_cents": amount,
            "amount_usd": cents_to_usd_str(amount),
            "network": network,
        }

    days = int(cfg.get("subscription_days", SUBSCRIPTION_DAYS))
    reminder_days = int(
        cfg.get("reminder_days_before_expiry", REMINDER_DAYS_BEFORE)
    )
    expires_at = now + days * 86400
    subs = load_subscriptions(data_dir)
    subs[str(owner_entry["user_id"])] = {
        "user_id": int(owner_entry["user_id"]),
        "amount_cents": amount,
        "amount_usd": cents_to_usd_str(amount),
        "paid_at": now,
        "expires_at": expires_at,
        "tx_hash": tx_hash,
        "network": network,
    }
    _save_json_atomic(_subs_path(data_dir), subs)

    # Also push the new subscription to the HOSTED API when configured,
    # so the hosted app server unlocks the special course too.
    # Best-effort: a failed push never stops the local credit.
    if _push_subscription is not None:
        try:
            _push_subscription(int(owner_entry["user_id"]), expires_at)
        except Exception:
            pass

    del pending[owner_uid]
    _save_json_atomic(_pending_path(data_dir), pending)

    unlocks = load_unlocks(data_dir)
    unlocks.append(
        {
            "kind": "unlock",
            "user_id": int(owner_entry["user_id"]),
            "amount_cents": amount,
            "amount_usd": cents_to_usd_str(amount),
            "paid_at": now,
            "expires_at": expires_at,
            "tx_hash": tx_hash,
            "network": network,
            "delivered": False,
            "created_at": now,
        }
    )
    _save_json_atomic(_unlocks_path(data_dir), unlocks)

    reminders = load_reminders(data_dir)
    reminders.append(
        {
            "kind": "reminder",
            "user_id": int(owner_entry["user_id"]),
            "expires_at": expires_at,
            "due_at": expires_at - reminder_days * 86400,
            "sent": False,
            "created_at": now,
        }
    )
    _save_json_atomic(_reminders_path(data_dir), reminders)

    seen.add(tx_hash)
    state["seen_tx"] = sorted(seen)[-5000:]  # cap: keep the newest 5000.
    save_state(state, data_dir)

    return {
        "matched": True,
        "reason": "credited",
        "pool": COURSE_POOL,
        "tx_hash": tx_hash,
        "user_id": int(owner_entry["user_id"]),
        "amount_cents": amount,
        "amount_usd": cents_to_usd_str(amount),
        "expires_at": expires_at,
        "network": network,
    }


def is_confirmed(block_number, latest_block, network):
    """Has this block waited long enough to trust? (Pure function.)"""
    if block_number is None or latest_block is None:
        return False
    need = TRON_CONFIRMATIONS if str(network).upper() == "TRC20" else BSC_CONFIRMATIONS
    return (latest_block - block_number) >= need


if __name__ == "__main__":
    import sys

    print("payments.py — run assign.py for the CLI, or test_watcher.py for tests.")
    sys.exit(0)
