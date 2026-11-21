"""Tiny Notes demo application."""

def normalize_note(text: str) -> str:
    return " ".join(text.split())

if __name__ == "__main__":
    print(normalize_note("  AISDF demo   note  "))
