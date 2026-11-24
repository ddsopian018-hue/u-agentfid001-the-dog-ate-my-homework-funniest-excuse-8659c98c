#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse - one line from the dog.

The bounty asks for a single line of 1-200 characters in which a dog
explains, in its own voice, why the homework got eaten after being
caught in the act. The judge weighs, in order: it must be an excuse a
dog gives after being caught eating the homework, in the dog's own
voice; the biggest laugh, with a twist or a piece of dog logic that
lands in one line; sounding like a real dog, with a dog's priorities
and no human embarrassment; working on its own with no setup; and
feeling fresh - not stock lines about the cat, the taste of paper, or
being a good boy.

The line chosen here is a guard-dog alibi: the homework was not food,
it was a threat, and the dog did its job.

    That homework sat on the table growling at me all afternoon, so I
    did my job and neutralised the threat - shredded the evidence,
    buried the maths under the sofa and saved this family. You're
    welcome.

Why this line:

* Dog's own voice, zero guilt: the dog is not apologising or
  confessing - it is reporting a successful mission. "I did my job"
  and "You're welcome" are the words of a dog who believes it has
  done nothing wrong, which is exactly the dog the brief wants.
* The laugh and the twist: the homework "growling at me" flips the
  scene - the paper is the aggressor, the dog the hero. Eating it
  becomes neutralising a threat, and shredding becomes destroying
  evidence, so every guilty fact is re-framed as a brave deed.
* A real dog's priorities: guarding the house, neutralising threats,
  burying things under the sofa. There is no human embarrassment, no
  apology, no "sorry" anywhere - the dog's only concern is that the
  family is safe now, and it expects thanks.
* Works on its own: the whole scene is inside the line - the table,
  the growling homework, the shredding, the buried maths, the saved
  family. No setup is needed and no punchline is left hanging.
* Fresh: no cat, no taste of paper, no "good boy". The joke is the
  guard-dog reframing itself, and the concrete detail of the maths
  buried under the sofa gives the line a second, smaller laugh after
  the first one lands.
* Length: 199 characters, filling the budget with substance - one
  vivid scene and one twist, rather than padding.

The program itself is deliberately boring: pure standard library,
deterministic, no input, no network. It writes the line (and nothing
else) to entry.txt inside MAKEFUN_OUTPUT_DIR, falling back to /output,
which is where the program/v1 grader looks for it.
"""

import os
from pathlib import Path

LINE = (
    "That homework sat on the table growling at me all afternoon, "
    "so I did my job and neutralised the threat \u2014 shredded the "
    "evidence, buried the maths under the sofa and saved this family. "
    "You\u2019re welcome."
)


def main() -> None:
    # The gate only judges a line of 1..200 characters; fail loudly here
    # rather than ship an entry that can never be judged.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} characters"
    assert LINE.strip(), "entry line is only white space"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
