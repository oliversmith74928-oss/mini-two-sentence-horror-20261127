#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun.

Writes the entry story (exactly two sentences, at most 400 characters)
to entry.txt inside the output directory given by MAKEFUN_OUTPUT_DIR.
Never writes anything into the repository directory itself.
"""

import os

STORY = (
    # Quiet, ordinary ritual in sentence one; the turn lands in sentence two.
    "Every night since the accident, my wife sets a plate for our son "
    "at his empty chair, and every morning she clears it away untouched. "
    "Last night the plate came back clean, and this morning there was a "
    "second plate on the table, set for me."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
