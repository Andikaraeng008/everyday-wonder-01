import os

TEXT = "The escalator carried me past my own reflection twice, and the second time it waved first."

# Gate: /output/entry.txt must be UTF-8, 1-200 chars, not whitespace-only.
assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "entry fails the 1-200 char gate"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
