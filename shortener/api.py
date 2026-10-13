"""HTTP-style handlers for the link shortener."""
from shortener import codes, store


def create_link(url: str) -> str:
    code = codes.make_code(url)
    store.save(code, url)
    return code


def resolve_link(code: str) -> str | None:
    return store.load(code)
