#!/usr/bin/env python3
"""make.fun entry: One Line of Wonder.

Writes one line — a small concrete thing made strange: the sound in a
seashell is your own blood, and the sea has never once corrected you —
to /output/entry.txt.
"""
import os

ENTRY = "The sound you hear when you press a shell to your ear is your own blood, and the sea has never once corrected you."

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200 characters,
# not only whitespace. Fail loudly here rather than ship invalid. The entry
# is pure ASCII, so its byte length equals its character length; assert both
# so a future edit cannot silently break the gate either way.
assert ENTRY == ENTRY.strip() and 1 <= len(ENTRY) <= 200, "entry violates the gate"
assert len(ENTRY.encode("utf-8")) == len(ENTRY) == 114, "entry must stay 114 bytes"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
