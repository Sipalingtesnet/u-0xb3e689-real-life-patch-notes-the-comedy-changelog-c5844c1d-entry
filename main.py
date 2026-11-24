"""Writes this entry's one-line patch note to /output/entry.txt.

Deterministic: the same bytes on every run, no network, stdlib only.
"""

import os

LINE = (
    "v3.2.0: fixed a bug where crossing a doorway clears the buffer "
    "holding the reason you came in; reason now written to disk, never read."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
