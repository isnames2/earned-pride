"""One Line of Earned Pride — writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python standard library only (os, pathlib). Deterministic: the same
bytes on every run.
"""

import os
from pathlib import Path

# The entry is 175 characters (1-240 allowed), no trailing newline.
LINE = (
    "The letter came on a Tuesday: her son, the boy who once couldn't read "
    "the bus timetable, had passed the bar. She folded it twice and put it "
    "in the drawer with the good spoons."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
