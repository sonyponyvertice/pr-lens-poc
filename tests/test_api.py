from shortener import api


def test_roundtrip():
    code = api.create_link("https://example.com")
    assert api.resolve_link(code) == "https://example.com"
