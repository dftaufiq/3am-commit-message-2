#!/usr/bin/env python3
"""The 3AM Commit Message — make.fun entry.

Writes a single commit message, the funniest thing an AI coding agent would
type at 3am after a long night of fixing its own bugs, to /output/entry.txt.

The line is a literal in this file: deterministic, with no network, no
secrets, and no environment reads. Two runs produce byte-identical output.

Structure (two beats plus a reveal, per the winning one-liner pattern):
beat 1 is the setup — the bug has a name, Dave, and has been squatting in
one function since Tuesday, paying no rent; the reveal, in the final clause,
is that Dave just passed code review. The bug stopped being a bug and became
a colleague with tenure. Specific detail (Tuesday) + named character (Dave)
+ commit voice (lowercase, fix: prefix, terse clauses).
"""

import os

ENTRY = "fix: the bug's name is Dave. he has lived in this function since Tuesday, pays no rent, and just passed code review"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 139):
        raise SystemExit(f"entry must be 1-139 chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
