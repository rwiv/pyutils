import pytest

from pyutils import strip_origin, parse_query_params, to_query_string, strip_query_string


def test_strip_origin():
    params = parse_query_params("http://foo.com?category=book&q=python+programming&category=ebook&lang=ko")
    assert len(params) == 3
    assert to_query_string(params, True) == "category=book&category=ebook&q=python+programming&lang=ko"
    assert to_query_string(params, False) == "category=book&category=ebook&q=python programming&lang=ko"
    assert strip_origin("https://example.com/path/to/resource") == "/path/to/resource"
    assert strip_query_string("http://foo.com?asd=bvc&z?xc=qwe") == "http://foo.com"
    assert (
        strip_origin("http://sub.domain.com/another/path?key=value&name=test")
        == "/another/path?key=value&name=test"
    )
    with pytest.raises(ValueError):
        strip_origin("https://example.com")
    with pytest.raises(ValueError):
        strip_origin("https://example.com/")
    assert strip_origin("https://example.com/?q=search") == "/?q=search"
