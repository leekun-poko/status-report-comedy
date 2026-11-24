"""Entry for make.fun's Status Report Comedy Sprint.

Writes one status-report line to /output/entry.txt, where the
grader's gate scorer and the house judge read it.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

LINE = (
    "Status: every task done exactly as specified, including the typo. "
    "The typo is now in production and officially outranks me."
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
