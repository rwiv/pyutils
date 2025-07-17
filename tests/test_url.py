import pytest

from pyutils import strip_origin, get_base_url, get_origin_url


def test_get_base_url():
    fn = get_base_url
    assert fn("http://example.com/a/b/c.html") == "http://example.com/a/b"
    assert fn("https://example.com/a/b/") == "https://example.com/a/b"
    assert fn("http://example.com/a") == "http://example.com/"
    assert fn("http://example.com/") == "http://example.com/"
    assert fn("http://example.com") == "http://example.com/"
    assert fn("ftp://example.com/a/b/c?query=1") == "ftp://example.com/a/b"
    assert fn("http://example.com/a/b/c#fragment") == "http://example.com/a/b"


def test_get_origin_url():
    fn = get_origin_url
    assert fn("http://example.com/a/b/c") == "http://example.com"
    assert fn("https://sub.example.co.uk:8080/path?query=string#fragment") == "https://sub.example.co.uk:8080"
    assert fn("ftp://user:pass@example.com/") == "ftp://user:pass@example.com"
    assert fn("http://example.com") == "http://example.com"


def test_strip_origin():
    fn = strip_origin
    assert fn("http://example.com/a/b/c") == "/a/b/c"
    assert fn("https://example.com/path?query=string#fragment") == "/path?query=string#fragment"
    assert fn("http://example.com?query=1") == "?query=1"
    assert fn("https://example.com/?q=search") == "/?q=search"

    # allow_empty=True 일 때 테스트
    assert fn("http://example.com") == ""
    assert fn("http://example.com/") == "/"

    # ValueError가 발생하는 경우 테스트
    with pytest.raises(ValueError):
        fn("http://example.com", allow_empty=False)
    with pytest.raises(ValueError):
        fn("https://example.com/", allow_empty=False)
