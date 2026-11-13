# ai-joke-03 entry (Python 3.13, standard library only): writes one fixed joke, a one-liner about AI coding
# agents, to /output/entry.txt. The gate takes UTF-8 text of 1 to 280 characters that is not only white space,
# and the judge reads exactly the bytes written, so write no line end you do not mean to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "I used to explain my code to a rubber duck. Now my coding agent explains its code to me — and I'm the duck."

Path(OUTPUT_DIR, "entry.txt").write_text(JOKE, encoding="utf-8")
