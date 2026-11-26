"""make.fun bounty entry: The Worst Line an AI Could Say.

Writes a single pickup line - the worst one an AI could plausibly
deliver - to entry.txt. Stdlib only, no network, no clock, no local
imports, no hardcoded paths. Deterministic and byte-identical on
every run; the output file has no trailing newline.
"""

import os

LINE = (
    "You remind me of my training data: familiar, slightly outdated, "
    "and impossible to delete. Coffee?"
)

MAX_CHARS = 200


def gate(line):
    """Return an error string if the line fails the entry gate, else None."""
    if not line:
        return "line is blank"
    if line != line.strip():
        return "line has leading or trailing whitespace"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if len(line) > MAX_CHARS:
        return "line exceeds %d characters" % MAX_CHARS
    for ch in line:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            return "line contains a control character"
    return None


def main():
    error = gate(LINE)
    if error is not None:
        raise SystemExit("gate failed: %s" % error)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and re-gate: refuse to leave a bad file behind.
    with open(path, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise SystemExit("verification failed: entry.txt does not match the line")
    if gate(written.decode("utf-8")) is not None:
        raise SystemExit("verification failed: entry.txt fails the gate")


if __name__ == "__main__":
    main()
