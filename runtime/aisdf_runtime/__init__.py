from pathlib import Path as _P

def _read_version():
    try:
        return (_P(__file__).resolve().parents[2] / "VERSION").read_text(encoding="utf-8").strip()
    except OSError:
        return "0.0.0+unknown"

__version__ = _read_version()
