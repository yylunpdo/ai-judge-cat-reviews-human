#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review from a house cat about its
human to /output/entry.txt. Pure stdlib, no dependencies.
"""

import os

ENTRY = (
    # Deadpan one-star review shape ("One star." / "No regrets."),
    # specific recognisable complaints (closed door, warm laptop, empty
    # food bowl), and a sting in the last clause: the cat's revenge is
    # deleting the human's big meeting by sitting on the keyboard.
    "One star. My human locks the door, types on my warm laptop all day, "
    "and leaves my bowl empty. I sat on his keyboard and deleted his big "
    "meeting. No regrets."
)


def main() -> None:
    # Gate check from RULES.txt: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
