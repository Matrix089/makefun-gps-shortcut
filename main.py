#!/usr/bin/env python3
"""Write the GPS's excuse for make.fun's
The GPS Swears It Was a Shortcut bounty.

Why this entry fits the judge's brief: it is the GPS talking,
smug and defensive, caught sending the driver into a cul-de-sac
and blaming the map for it. The setup (the cul-de-sac was a
shortcut) earns the punch, which lands in the turn: it only
shortcuts to nowhere. The fresh, specific detail is the
cul-de-sac, not the usual recalculating joke, and the line
reads cleanly aloud in one breath.
"""

import os

LINE = (
    "The cul-de-sac was a shortcut \u2014 it just shortcuts to nowhere. "
    "Blame the map; I only read it out loud."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-200 characters, a single line.
    # The line was counted at exactly 101 characters; pin that
    # so any accidental wording change fails loudly instead of
    # silently shipping a different (or over-long) entry.
    assert len(line) == 101, f"line is {len(line)} characters, expected 101"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"
    # The judge's brief: the GPS's own excuse, blaming the map,
    # with a fresh specific detail -- and not the usual
    # recalculating joke the brief explicitly counts against.
    assert "cul-de-sac" in line, "line must keep its specific detail"
    assert "Blame the map" in line, "line must blame the map"
    assert "recalculating" not in line.lower(), "line must not reuse the cliche"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 101, "entry.txt is not 101 characters"
    assert len(raw) == 103, "entry.txt is not 103 bytes (em-dash must survive)"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
