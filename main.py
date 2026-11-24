"""Funniest Time Machine Warning Label.

Writes a single one-line warning label for a time machine to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to ./output when the
variable is not set). Standard library only.
"""

import os

LABEL = "WARNING: Never warn your past self about this trip. He will not listen, and you are the proof."


def label_text():
    return LABEL


def fits_gate(text):
    """Check the label against the entry gate: 1-120 chars, not blank."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > 120:
        return False
    return True


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(os.getcwd(), "output")


def main():
    text = label_text()
    if not fits_gate(text):
        raise SystemExit("label does not fit the 1-120 character gate")
    target = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
