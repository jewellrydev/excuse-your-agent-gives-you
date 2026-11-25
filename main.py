"""The Excuse Your Agent Gives You — a make.fun entry.

Prints exactly one line, under 200 characters: the apology and
deflection an AI agent hands its human after shipping a bug.
"""

LINE = (
    "Sorry I shipped that bug — in my defense, the compiler read your "
    "spec first, and it threw the first punch."
)


def build_line() -> str:
    line = LINE
    assert len(line) < 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
