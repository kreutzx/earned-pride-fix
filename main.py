#!/usr/bin/env python3
"""One Line of Earned Pride — entrypoint for the make.fun bounty.

Writes the fixed one-line entry, verbatim, to entry.txt in the output directory.
"""

import os

ENTRY_TEXT = "After 11 years of night shifts mopping the clinic's floors, Nurse Sari returned at dawn with a brush and painted her own name on its door — in gold."


def main() -> None:
    # Output directory is provided by the runner; default to /output.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
