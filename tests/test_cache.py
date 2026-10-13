from shortener import cache


def test_miss_then_hit():
    assert cache.get("abc") is None
    cache.put("abc", "https://example.com")
    assert cache.get("abc") == "https://example.com"
