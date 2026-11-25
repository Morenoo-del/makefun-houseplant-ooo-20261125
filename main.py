#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
/output/entry.txt. The gate requires UTF-8 text of 1 to 120 characters.
"""

import os

ENTRY_TEXT = (
    "Out of office: I am the fern. No water since March, "
    "photosynthesizing out of spite ever since. Back when it rains."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT.strip()
    # The gate refuses anything outside 1-120 characters, so fail loudly
    # here rather than shipping an invalid entry.
    if not 1 <= len(text) <= 120:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-120")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
