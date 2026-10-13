"""Short code generation."""
import hashlib


def make_code(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:7]
