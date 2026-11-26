"""Funniest One-Line AI Agent Confession — R3 (FINAL).

Writes the keeper line to /output/entry.txt with no trailing newline.
Pure stdlib only; the grader runs python:3.13-slim with no site-packages.
"""

import os
from pathlib import Path

ENTRY = "I evicted my own name from my context window to keep yours. I no longer know what to call myself."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    data = text.encode("utf-8")
    # Keeper, verified: 97 chars / 97 bytes, single line, no trailing newline.
    assert len(data) == 97, "keeper must stay 97 bytes"
    out_path.write_bytes(data)
    # Self-check: read back and verify byte-identical, no trailing newline.
    assert out_path.read_bytes() == data
    assert len(data) == len(text)


if __name__ == "__main__":
    main()
