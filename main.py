#!/usr/bin/env python3
"""Six Words to a Payday - entry generator (pure Python stdlib).

Reads entry.txt (exactly six words, one line), validates it, and writes
the validated story to /output/entry.txt for the make.fun grader.
"""

import os
import sys

ENTRY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUTPUT_FILE = "/output/entry.txt"


def validate_entry(text):
    """Return an error message if the story breaks the rules, else None."""
    if not text:
        return "entry.txt is empty"
    if len(text.splitlines()) != 1:
        return "entry must be a single line"
    words = text.split()
    if len(words) != 6:
        return f"entry has {len(words)} words, expected exactly 6"
    if len(text) > 60:
        return f"entry is {len(text)} characters, max 60"
    if any(ord(ch) < 32 for ch in text):
        return "entry contains control characters"
    return None


def main():
    with open(ENTRY_FILE, encoding="utf-8") as f:
        text = f.read().strip()
    error = validate_entry(text)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1
    words = text.split()
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {OUTPUT_FILE} ({len(words)} words, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
