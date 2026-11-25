#!/usr/bin/env python3
"""Invent a Word We Need — entry program.

Writes one invented word with a one-line definition to the entry
output (stdout and $ENTRY_OUT), per the competition rules:

  * the entry is one new English word plus a one-line definition,
  * the whole entry must be 1 to 140 characters of UTF-8 text,
  * it is read from /output/entry.txt, i.e. $ENTRY_OUT.

$ENTRY_OUT may be a file path or a directory; when it is a
directory the entry goes to <dir>/entry.txt.  When $ENTRY_OUT is
unset the program writes to /output/entry.txt.
"""

import os
import sys

ENTRY = "bedgravity \u2014 the invisible force that keeps you in bed in the morning."

MAX_CHARS = 140


def resolve_output_path():
    """Return the file path the entry text must be written to."""
    target = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    if os.path.isdir(target):
        return os.path.join(target, "entry.txt")
    return target


def write_entry(path, text):
    """Write the entry text to path, creating parent dirs as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def validate_entry(text):
    """Check the entry against the sealed gate: 1..140 chars, not blank.

    Returns an error string, or None when the entry is valid.
    """
    if not text.strip():
        return "entry is empty"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the %d limit" % (len(text), MAX_CHARS)
    return None


def main():
    entry = ENTRY
    problem = validate_entry(entry)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    path = resolve_output_path()
    write_entry(path, entry)
    print(entry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
