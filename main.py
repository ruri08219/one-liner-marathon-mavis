#!/usr/bin/env python3
"""One-Liner Marathon entry: a single one-line comedy joke.

Writes the joke to /output/entry.txt (or $ENTRY_OUTPUT when set, for
local testing). Standard library only.
"""

import os
from pathlib import Path

JOKE = (
    "My password manager forgot my master password, so now we just stare "
    "at each other like a couple that ran out of things to say."
)


def main() -> None:
    # The gate only accepts 1-280 characters: refuse to write an entry
    # that could never be judged instead of silently shipping it.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise SystemExit(f"entry must be 1-280 chars, got {len(JOKE)}")
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
