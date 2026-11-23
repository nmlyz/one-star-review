#!/usr/bin/env python3
"""Write a one-line, one-star review of an everyday essential to a text file.

The program writes exactly one review, a single line of at most 160
characters, to ``entry.txt`` inside the output directory. The output
directory is ``MAKEFUN_OUTPUT_DIR`` when that environment variable is set,
and ``/output`` otherwise. The output file is written with mode 0644.

Standard library only, no network, fully deterministic: every run writes
the same bytes.
"""

import os
import stat

REVIEW = (
    "Gravity never clocks out, never takes a holiday, and still cannot "
    "keep my socks from sliding down inside my shoes."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    data = REVIEW.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Sanity check: the review must satisfy the gate (1-160 chars, UTF-8).
    assert 1 <= len(REVIEW) <= 160, len(REVIEW)


if __name__ == "__main__":
    main()
