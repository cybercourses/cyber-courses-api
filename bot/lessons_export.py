#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the free-lessons JSON payload from bot/lessons.py.

Single source of truth for the lesson content shape. Two consumers:
  * app/tools/export_lessons.py — writes assets/lessons.json (bundled
    in the APK so the app works offline).
  * app/server/app.py — GET /lessons (so the app can refresh its lessons
    from the server when online, with no new APK).

The special (paid) course in special_lessons.py is NEVER included here:
it stays locked for subscribers only and is served only by
GET /special-lessons after a subscription check.

Payload shape (identical to the bundled asset):
    {"app": ..., "app_en": ..., "version": ..., "tracks": [
        {"id", "emoji", "name_ar", "name_en", "lessons": [
            {"title_ar", "title_en", "ar", "en"}, ...]}, ...]}
17 tracks, 176 lessons.
"""

import os
import sys

# Bot callback order (bot.py menu) — ids + emojis, in the order tracks
# first appear in lessons.ALL_LESSONS.
TRACK_META = [
    ("cyber", "🛡️"),
    ("python", "🐍"),
    ("ruby", "💎"),
    ("networks", "🌐"),
    ("htmlcss", "🎨"),
    ("sql", "🗄️"),
    ("sqli", "💉"),
    ("ai", "🤖"),
    ("freelance", "💰"),
    ("data", "📊"),
    ("marketing", "📣"),
    ("mobile", "📱"),
    ("linux", "🐧"),
    ("js", "🟨"),
    ("design", "🎬"),
    ("cloud", "☁️"),
    ("ecommerce", "🛒"),
]

PAYLOAD_VERSION = "1.0.0"


def build_tracks_payload():
    """Return the free-lessons payload dict, built fresh from lessons.py.

    Raises AssertionError if the content does not match the expected
    shape (17 tracks / 176 lessons, every lesson complete). Callers
    that serve this over the network should catch that and answer 500.
    """
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import lessons  # noqa: E402  (bot content module, read-only import)

    all_lessons = lessons.ALL_LESSONS
    assert len(all_lessons) == 176, \
        "expected 176 lessons, got %d" % len(all_lessons)

    # Ordered unique tracks, in first-appearance order.
    ordered = []
    seen = set()
    for lesson in all_lessons:
        key = (lesson["track_ar"], lesson["track_en"])
        if key not in seen:
            seen.add(key)
            ordered.append(key)
    assert len(ordered) == 17, "expected 17 tracks, got %d" % len(ordered)
    assert len(TRACK_META) == 17

    tracks = []
    total = 0
    for (track_ar, track_en), (track_id, emoji) in zip(ordered, TRACK_META):
        track_lessons = [l for l in all_lessons if l["track_ar"] == track_ar]
        assert track_lessons, "empty track %s" % track_id
        assert "خاص" not in track_ar, \
            "special course must never be exported"
        for l in track_lessons:
            for field in ("title_ar", "title_en", "ar", "en"):
                assert isinstance(l[field], str) and l[field].strip(), \
                    "bad field %s in %s" % (field, track_id)
                assert len(l[field]) < 4096, \
                    "lesson too long: %s %s" % (track_id, l["title_ar"])
        total += len(track_lessons)
        tracks.append({
            "id": track_id,
            "emoji": emoji,
            "name_ar": track_ar,
            "name_en": track_en,
            "lessons": [
                {
                    "title_ar": l["title_ar"],
                    "title_en": l["title_en"],
                    "ar": l["ar"],
                    "en": l["en"],
                }
                for l in track_lessons
            ],
        })

    assert total == 176, "expected 176 total, got %d" % total
    return {
        "app": "دورات الأمن السيبراني 🛡️",
        "app_en": "Cybersecurity Courses",
        "version": PAYLOAD_VERSION,
        "tracks": tracks,
    }


if __name__ == "__main__":
    import json

    payload = build_tracks_payload()
    print("OK: %d tracks, %d lessons"
          % (len(payload["tracks"]),
             sum(len(t["lessons"]) for t in payload["tracks"])))
