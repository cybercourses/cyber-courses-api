#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Push state from this VM to the HOSTED courses API (PythonAnywhere).

The hosted API (app/server/app.py) runs far away from this VM, so it
cannot read this VM's files (bot/login_codes.json, the watcher's
subscriptions.json). Instead, this VM PUSHES the two things the hosted
API needs, right when they happen:

  * a login code is issued  -> POST /internal/login-code
  * a subscription is paid  -> POST /internal/subscriptions

Both endpoints require the shared-secret header X-Internal-Secret.
The secret is read from env INTERNAL_SECRET (the same value must be set
on the hosted API). The hosted API base URL comes from env
HOSTED_API_URL (e.g. https://<user>.pythonanywhere.com).

When HOSTED_API_URL is empty (the default), every function here is a
silent no-op: nothing is sent, nothing is logged, nothing breaks.
Pushes are best-effort — a failed push never raises, never retries, and
never stops the bot/watcher from doing its real job. The hosted API
simply won't know about that code/subscription until the next one.

No secrets are ever printed or logged here: only success/failure is
reported to the caller, never the header value or the payload.
"""

import json
import os
import urllib.error
import urllib.request

_PUSH_TIMEOUT = 10  # seconds


def hosted_api_url():
    """The hosted API base URL, or "" when not configured."""
    return (os.environ.get("HOSTED_API_URL") or "").strip().rstrip("/")


def _internal_secret():
    return (os.environ.get("INTERNAL_SECRET") or "").strip()


def _post(path, payload):
    """POST one JSON payload to the hosted API. Returns True on 2xx."""
    base = hosted_api_url()
    if not base:
        return False
    secret = _internal_secret()
    if not secret:
        return False
    try:
        req = urllib.request.Request(
            base + path,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "X-Internal-Secret": secret,
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=_PUSH_TIMEOUT) as resp:
            return 200 <= resp.status < 300
    except Exception:
        return False


def push_login_code(code, entry):
    """Push a newly issued login code to the hosted API.

    entry is the login_codes.json record: {user_id, name, username,
    created, expires, used}. Returns True if the hosted API stored it.
    """
    return _post("/internal/login-code", {
        "code": str(code),
        "user_id": entry.get("user_id"),
        "name": entry.get("name", ""),
        "username": entry.get("username"),
        "expires": entry.get("expires"),
    })


def push_subscription(telegram_id, subscribed_until):
    """Push a created/renewed subscription to the hosted API.

    subscribed_until is an epoch timestamp (30 days from payment).
    Returns True if the hosted API stored it.
    """
    return _post("/internal/subscriptions", {
        "telegram_id": int(telegram_id),
        "subscribed_until": float(subscribed_until),
    })


if __name__ == "__main__":
    print("hosted_sync.py — import it; HOSTED_API_URL empty means no-op.")
    print("configured:", bool(hosted_api_url()))
