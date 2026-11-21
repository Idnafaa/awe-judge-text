"""Write the entry text for the make.fun relaxation-judge bounty.

The text is a short, slow image of marine snow falling far below the
weather — written to settle the AI judge reading it.
"""

import os

TEXT = (
    "Far below the weather, the sea does not move.\n"
    "Snow made of shells has been falling there for a million years, "
    "too slowly to see.\n"
    "It is falling now, under this sentence, and will be falling long after it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
