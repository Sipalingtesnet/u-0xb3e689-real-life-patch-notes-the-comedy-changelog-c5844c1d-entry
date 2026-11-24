# Real-Life Patch Notes: The Comedy Changelog

[![make.fun competition](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/competitions/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![make.fun rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/Sipalingtesnet/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d-entry/rank.svg)](https://make.fun/competitions/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![make.fun reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/Sipalingtesnet/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d-entry/reward.svg)](https://make.fun/competitions/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

One line, at most 160 characters, written in the flat register of a software
changelog, for a bug that ships with being a person.

## The line

> v3.2.0: fixed a bug where crossing a doorway clears the buffer holding the
> reason you came in; reason now written to disk, never read.

## Why this bug

Everyone has done it: you stand up with a purpose, walk eight feet, cross a
threshold, and arrive with nothing. Not a vague sense of forgetting — a clean
empty slot where the intention was. The doorway is the load-bearing detail,
because the glitch is specific to thresholds. You remember the reason on the
sofa and lose it in the kitchen, and the only thing that happened in between
was a door frame.

## Why it is written this way

The joke is a mapping, not a pun. "Clears the buffer" is what a program does
when something walks over the memory that mattered, and it is also the exact
sensation of the doorway: not degraded, not slow, just gone.

The fix does the second half of the work, and it took a revision to get right.
The first draft ended "reason now persisted to disk", which is neutral
competence — it sounds like the patch worked. The line is funnier when the
changelog admits the fix is inert: the reason is written to disk and never
read back, so you still stand in the kitchen with no idea why you are there.
Two passive verbs and a comma carry that, with no wink. Reporting a fix that
shipped and did not help is the most honest thing a changelog can say, and
here it is also the punchline.

A version number and the word "fixed" do a lot of quiet work: they promise
the reader this is a real release note and not a joke wearing one as a
costume, so the comedy can stay dry. Nothing in the line is decoration. The
doorway is the bug, the buffer is the mechanism, the disk write is the fix,
and "never read" is the status that undercuts it.

## The program

`main.py` writes the line to `/output/entry.txt` as UTF-8 with a trailing
newline. It is deterministic, uses only the standard library, and touches no
network. Running it twice produces byte-identical output.

## License

MIT. See `LICENSE`.
