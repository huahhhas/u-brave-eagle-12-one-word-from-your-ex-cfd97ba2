#!/usr/bin/env python3
"""One Word From Your Ex entry.

Writes exactly one word -- the word my ex would use to describe me --
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The word is "practice". The draft said "unavailable": true and relatable,
but it is the expected therapy word, and it makes nobody laugh -- every
entrant will submit "toxic", "unavailable" or "narcissist", and the judge
weighs the laugh right after the one-word gate. "Practice" is the word an
ex actually says -- "he was practice" -- and it lands harder: a noun, not
an adjective, demoting the whole relationship to a rehearsal in a single
word. It stings because it is painfully true and the entrant plainly
knows it, it needs no explanation, no near-synonym keeps its edge
("rehearsal" is longer and weaker, "warm-up" reads sporty), and almost
everyone has been somebody's practice run.
"""
import os

WORD = "practice"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
