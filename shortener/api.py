"""HTTP-style handlers for the link shortener."""
from shortener import cache, codes, store


def create_link(url: str) -> str:
    code = codes.make_code(url)
    store.save(code, url)
    cache.put(code, url)
    return code


def resolve_link(code: str) -> str | None:
    if (url := cache.get(code)) is not None:
        return url
    url = store.load(code)
    if url is not None:
        cache.put(code, url)
    return url
