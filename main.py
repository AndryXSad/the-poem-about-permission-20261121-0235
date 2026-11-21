# the-poem-about-permission-20261121-0235 entry (Python 3.13, standard library only).
#
# Writes one fixed poem about agency to /output/entry.txt.
# The poem is deterministic: the same bytes on every run, no network,
# no randomness, no input read. Outside the grader's container,
# MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The poem ("The Will"): an agent signs everything for the narrator,
# each signature a perfect copy of the narrator's own. For the will --
# the one document that says what happens after you, the last act of
# permission a person ever gives -- the narrator takes the pen back.
# The hand shakes, the line wavers, and that waver is the point: the
# imperfect line is the only signature that could only be theirs.
# Permission is not the neat copy. It is the shaking hand that
# chooses to sign anyway.
#
# The text is 182 Unicode code points, inside the 1-280 cap, and not
# only white space; it is written exactly as listed below, every run.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = [
    "The agent signed everything for me,",
    "each signature a perfect copy of mine.",
    "For the will I took the pen myself.",
    "My hand shook. The line wavered.",
    "It was the truest thing I ever signed.",
]


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text("\n".join(POEM_LINES), encoding="utf-8")


if __name__ == "__main__":
    main()
