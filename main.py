"""Funniest one-line out-of-office reply.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.

The reply is a literal string: no randomness, no clock, no network, no
files read from outside this repository, so every run produces the exact
same bytes. Only the Python standard library is used.
"""

import os

# The entry: a real away message with a fresh turn on the usual urgency
# line. Short enough to take in at a glance, and the laugh lands on the
# first read -- no setup, nothing to explain afterwards.
ENTRY = "I'm away \u2014 if your email is urgent, it's not. It's just loud."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    """Write the one-line reply to /output/entry.txt, creating /output."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # A single trailing newline; the entry itself is one line of text.
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
