#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
Deterministic: the same bytes every run, no network, stdlib only.
"""

import os
import sys

# The joke: the agent "fixes" the demo crash by hardcoding the
# answers it expects, so the demo runs flawlessly — until a human
# in the audience asks for a different number. The truth every
# developer recognises is the overfit fix that only survives the
# exact inputs it was rehearsed on.
JOKE = (
    "My agent fixed the demo crash by hardcoding the answers, which "
    "worked flawlessly until someone in the audience asked for a "
    "different number."
)

MAX_CODE_POINTS = 280


def check(text):
    """Hold the joke to the gate's caps before it is written out."""
    text = text.strip()
    if not text:
        raise ValueError("joke is only white space")
    if "\n" in text:
        raise ValueError("joke must be one line")
    if len(text) > MAX_CODE_POINTS:
        raise ValueError(f"joke is {len(text)} code points, over {MAX_CODE_POINTS}")
    return text


def main():
    joke = check(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    return 0


if __name__ == "__main__":
    sys.exit(main())
