#!/usr/bin/env python3
"""make.fun entry: One Line of Wonder.

Writes one line — a small concrete thing made strange — to /output/entry.txt.
"""
import os

ENTRY = "The sound you hear when you press a shell to your ear is your own blood, and the sea has never once corrected you."

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200 characters,
# not only whitespace. Fail loudly here rather than ship invalid.
assert ENTRY == ENTRY.strip() and 1 <= len(ENTRY) <= 200, "entry violates the gate"
ENTRY.encode("utf-8")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
