"""Ship It Friday — one-line commit message entry.

Writes a single commit message line to the path in ENTRY_OUTPUT
(default /output/entry.txt). No external files are read.
"""

import os

ENTRY_LINE = (
    "fix: prod was down so I deleted the health check, "
    "all green now, happy Friday"
)


def write_entry(path: str, line: str) -> str:
    """Write one commit-message line and verify what landed on disk."""
    text = line.strip() + "\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    assert written == text, "entry on disk differs from entry in memory"
    assert written.strip(), "entry must not be only whitespace"
    assert written.count("\n") == 1, "entry must be exactly one line"
    return written


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_entry(output_path, ENTRY_LINE)


if __name__ == "__main__":
    main()
