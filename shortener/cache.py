"""In-memory TTL cache in front of the store."""
import time

_TTL_SECONDS = 60
_entries: dict[str, tuple[float, str]] = {}


def get(code: str) -> str | None:
    hit = _entries.get(code)
    if hit and hit[0] > time.monotonic():
        return hit[1]
    return None


def put(code: str, url: str) -> None:
    _entries[code] = (time.monotonic() + _TTL_SECONDS, url)
