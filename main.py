"""Everyday Things, Two Lines -- entry program.

Writes one two-line explanation to /output/entry.txt:
line 1 explains a queue to a 10-year-old through a caterpillar analogy,
line 2 says honestly what the analogy maps and what it leaves out.
"""

import os

LINE_1 = (
    "A queue is a caterpillar made of people, where each person is one "
    "segment that can only shuffle forward when the head takes a step."
)
LINE_2 = (
    "It maps how the whole line moves in small steps from the front, but "
    "leaves out that real caterpillars never get bored, push ahead, or "
    "wander off for a snack."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    # Mirror the competition gate: 1-400 chars of UTF-8 text, not only
    # whitespace, so a bad entry fails loudly here instead of at grading.
    body = text.strip()
    if not body or len(text) > 400:
        raise SystemExit(f"entry fails the gate: {len(text)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
