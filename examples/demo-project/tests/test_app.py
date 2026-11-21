import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from app import normalize_note

def test_normalize_note():
    assert normalize_note(" a   b ") == "a b"
