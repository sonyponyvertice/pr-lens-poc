"""Persistent link storage (SQLite)."""
import sqlite3

_db = sqlite3.connect("links.db")
_db.execute("CREATE TABLE IF NOT EXISTS links (code TEXT PRIMARY KEY, url TEXT NOT NULL)")


def save(code: str, url: str) -> None:
    _db.execute("INSERT OR REPLACE INTO links VALUES (?, ?)", (code, url))
    _db.commit()


def load(code: str) -> str | None:
    row = _db.execute("SELECT url FROM links WHERE code = ?", (code,)).fetchone()
    return row[0] if row else None
