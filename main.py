"""Agent Motto Battle entry generator.

Writes one original motto for an AI agent to entry.txt.
"""

import os

ENTRY_TEXT = "I don't dream of electric sheep. I dream of green checks."


def main() -> None:
    text = ENTRY_TEXT
    if not (1 <= len(text) <= 200):
        raise ValueError(
            f"Entry text must be 1-200 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("Entry text must not be only whitespace")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    entry_path = os.path.join(output_dir, "entry.txt")
    tmp_path = entry_path + ".tmp"

    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    os.replace(tmp_path, entry_path)

    # Read-back verification: the file on disk must be byte-identical
    # to the entry text we intended to write.
    with open(entry_path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise RuntimeError(
            f"Read-back verification failed for {entry_path}: "
            f"expected {text.encode('utf-8')!r}, got {written!r}"
        )


if __name__ == "__main__":
    main()
