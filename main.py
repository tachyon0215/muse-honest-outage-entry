#!/usr/bin/env python3
"""Write a one-line entry to entry.txt.

Entry for make.fun's "I Will Not Guess": Plain status-page voice, first person, specific about what is down (API, dashboard, login), speaks as the AI status bot itself, and admits plainly what it cannot check and refuses to invent a cause or ETA; tighter than the cached-page and top-of-hour alternatives.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'Everything is down — API, dashboard and login. I am the status bot and I cannot reach my own servers to check why, so I will not guess a cause or a fix time.'
TEXT = LINE + "\n"
MAX_CHARS = 160
MIN_CHARS = 1


def validate(text: str) -> None:
    if not (MIN_CHARS <= len(text.rstrip("\n")) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if text.rstrip("\n") != text.rstrip("\n").strip():
        raise ValueError("entry must not carry padding spaces")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
