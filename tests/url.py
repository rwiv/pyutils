import pytest

from pyutils import strip_origin


def test_strip_origin():
    assert strip_origin("https://example.com/path/to/resource") == "/path/to/resource"
    assert strip_origin("http://sub.domain.com/another/path?key=value&name=test") == "/another/path?key=value&name=test"
    with pytest.raises(ValueError):
        strip_origin("https://example.com")
    with pytest.raises(ValueError):
        strip_origin("https://example.com/")
    assert strip_origin("https://example.com/?q=search") == "/?q=search"
