# Deploy the courses API on Render (free tier)

Last updated: 2026-11-24. **No secrets in this file** — values marked
`<...>` must be filled in at deploy time, never committed here.

This folder is a clean, self-contained copy of the hosted API — the
alternative to PythonAnywhere (whose email verification was broken on
2026-11-24: its own "Resend email" button returns a server error).
`server/app.py` is an exact, unmodified copy of
`app/server/app.py`; only the files the API needs are here.

## What is in this folder

| File | Why it is here |
|---|---|
| `server/app.py` | The Flask API (exact copy, unmodified). |
| `server/` (runtime) | The hosted JSON stores are created here at runtime: `hosted_login_codes.json`, `hosted_subscriptions.json`, `hosted_payment_info.json` (git-ignored, never commit them). |
| `bot/lessons.py` | The 176 free lessons (content source). |
| `bot/lessons_export.py` | Builds the `GET /lessons` payload from `lessons.py`. |
| `bot/special_lessons.py` | The 35 paid lessons — served ONLY by `GET /special-lessons` after a subscription check, never in `/lessons`, never in the APK. |
| `bot/hosted_sync.py` | Push client used by `payments.py` (stdlib only). |
| `payment-watcher/payments.py` | Imported by `app.py`; in hosted mode the API reads the hosted stores, not this module's files. |
| `requirements.txt` | `Flask==3.1.3`, `gunicorn==27.0.1` (exact versions tested locally). |
| `render.yaml` | Blueprint: free plan, Frankfurt, build + start commands, `API_HOSTED_MODE=1`, `PYTHON_VERSION=3.12.0`. `INTERNAL_SECRET` is `sync: false` — set it in the dashboard, never here. |
| `.gitignore` | Keeps the runtime `hosted_*.json` stores out of git. |

The folder mirrors the original relative layout (`server/` next to
`bot/` and `payment-watcher/`) on purpose: `app.py` finds its lesson
and watcher files by relative paths, so it runs here with zero code
changes.

## Render free tier — facts (verified 2026-11-24 from Render's own docs)

Sources: https://render.com/docs/free and
https://render.com/docs/web-services (read 2026-11-24).

- **Free web services exist, no credit card required.** 512 MB RAM,
  0.1 CPU. 750 free instance hours per workspace per month (enough
  for one service running 24/7; spun-down services do not consume
  hours).
- **A Git repo is REQUIRED.** A web service deploys from a linked Git
  provider repo (GitHub / GitLab / Bitbucket), a public Git repo URL,
  or a prebuilt Docker image. There is no direct file upload. So the
  deploy-time step is: push this folder to a GitHub repo first.
- **It sleeps.** A free web service spins down after **15 minutes**
  without inbound traffic; the next request spins it back up in
  **about 1 minute** (Render shows a loading page to browsers while
  it wakes). Paid plans do not spin down.
- **⚠️ EPHEMERAL FILESYSTEM — the big caveat.** Render docs:
  "any changes to your web service's filesystem are *lost* every time
  the service redeploys, restarts, or spins down" — and free services
  *cannot* attach a persistent disk. Our hosted stores
  (`hosted_login_codes.json`, `hosted_subscriptions.json`,
  `hosted_payment_info.json`) are plain files next to `app.py`, so a
  spin-down or restart **wipes every pushed login code and every paid
  subscription** until they are pushed again.
  - Login codes are short-lived (10 min) anyway, so losing them is
    harmless.
  - Subscriptions are the real risk: a wiped store makes a paying
    subscriber look "not subscribed" until the watcher re-pushes.
  - **Mitigation (required): keep the service awake.** Ping
    `GET /health` at least every 10 minutes — e.g. a free UptimeRobot
    monitor, or a cron on this VM (`*/10 * * * * curl -s
    https://<name>.onrender.com/health`). A ping prevents spin-down,
    so the files survive. It does NOT protect against a Render
    restart/redeploy — after one of those, subscriptions must be
    re-pushed (follow-up work: make the watcher re-push all live
    subscriptions on startup; not done yet).
  - PythonAnywhere free does NOT spin down and keeps its files — that
    is why it was the first choice. Render is the fallback while its
    email verification is broken.
- **URL pattern:** `https://<service-name>.onrender.com` (automatic
  HTTPS, free). The service must bind `0.0.0.0:$PORT` (Render sets
  `$PORT` itself).
- Render may restart a free service at any time, and may suspend it
  for uncommonly high service-initiated traffic (our API makes none).

## Deploy steps (dashboard)

1. **Push this folder to GitHub.** Create a repo (e.g.
   `cyber-courses-api`), push the contents of `render-deploy/` to
   its `main` branch. (GitHub signup needs a working email —
   Gmail works fine.)
2. **Sign up at https://render.com** (free; Google sign-in works, no
   email-verification gate like PythonAnywhere's).
3. **Dashboard → New → Blueprint** (or New → Web Service for manual
   setup). Connect the GitHub repo. Render auto-detects `render.yaml`.
   - Service name: `cyber-courses-api` (URL becomes
     `https://cyber-courses-api.onrender.com`).
   - Plan: **Free**. Region: Frankfurt.
   - If doing it manually instead of the Blueprint:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn --chdir server app:app --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120`
     - Health Check Path: `/health`
4. **Set the secret.** Dashboard → the service → Environment →
   add: `INTERNAL_SECRET=<a long random string, 32+ letters/digits>`.
   Generate it now (e.g. `python3 -c "import secrets; print(secrets.token_urlsafe(32))"`)
   and keep it somewhere safe. `API_HOSTED_MODE=1` and
   `PYTHON_VERSION=3.12.0` already come from `render.yaml`.
   **Never put the real secret in any file in this repo.**
5. **Deploy.** First build takes a few minutes. When it is live, test:
   ```bash
   curl https://cyber-courses-api.onrender.com/health
   # {"hosted":true,"ok":true}
   curl -s https://cyber-courses-api.onrender.com/lessons | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d['tracks']), sum(len(t['lessons']) for t in d['tracks']))"
   # 17 176
   curl "https://cyber-courses-api.onrender.com/subscription?telegram_id=1817814526"
   # {"ok":true,"subscribed":true,...}  (owner is always subscribed)
   curl "https://cyber-courses-api.onrender.com/subscription?telegram_id=12345"
   # {"ok":true,"subscribed":false,...}
   ```
6. **Keep it awake (required, see caveat above).** Set up a free
   UptimeRobot monitor (or a cron on this VM) pinging
   `https://cyber-courses-api.onrender.com/health` every 10 minutes.
7. **Point the bot + watcher at it (on THIS VM).** Same as the
   PythonAnywhere step: set `HOSTED_API_URL=https://cyber-courses-api.onrender.com`
   and `INTERNAL_SECRET=<the SAME value as on Render>` for the bot
   and watcher services (protected EnvironmentFile, 600 perms),
   `systemctl daemon-reload`, restart both services. From then on
   every `/login` code and every paid subscription is pushed to
   Render automatically.
8. **Verify end-to-end:** send `/login` to the bot, verify the code
   against the hosted `/verify-code`; check `/subscription` and
   `/special-lessons` (35 lessons for the owner, 403 for a stranger).

## After the hosted API is live — rebuild the app

Same as for PythonAnywhere (see `DEPLOY_NOTES.md`): in
`app/lib/main.dart` set the ONE constant
`kDefaultServerUrl = 'https://cyber-courses-api.onrender.com'`,
rebuild the release APK, re-run `flutter test`, upload it, update
`APP_DOWNLOAD_URL` in `bot/bot.py`, restart the bot. New lessons then
reach users with NO new APK — but note: on Render, updating
`bot/lessons.py` means pushing the new copy to GitHub and letting
Render redeploy (a redeploy wipes the hosted stores, so re-push
subscriptions afterwards — see the caveat above).

## Local test (what was verified 2026-11-24)

From this folder, hosted mode on a test port:
```bash
cd render-deploy
API_HOSTED_MODE=1 INTERNAL_SECRET=test-internal-secret-for-local-check-only \
  gunicorn --chdir server app:app --bind 127.0.0.1:5055 --workers 1 --threads 4 --timeout 120
curl http://127.0.0.1:5055/health            # {"hosted":true,"ok":true}
curl http://127.0.0.1:5055/lessons           # 17 tracks, 176 lessons
curl "http://127.0.0.1:5055/subscription?telegram_id=1817814526"  # subscribed:true
curl "http://127.0.0.1:5055/subscription?telegram_id=12345"       # subscribed:false
```
Tested 2026-11-24: `/health` hosted:true, `/lessons` 17 tracks /
176 lessons, owner subscribed, stranger not subscribed, `/internal/*`
rejects a wrong secret (401) and hosted mode without a real
`INTERNAL_SECRET` refuses (503). No message was sent to the Telegram
group; `bot/state.json` was not touched.
