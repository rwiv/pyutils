from pyutils import merge_query_string, strip_query_string


def test_strip_query_string():
    fn = strip_query_string
    assert fn("http://example.com/path?query=1&a=2") == "http://example.com/path"
    assert fn("https://example.com/a/b/c?key=value") == "https://example.com/a/b/c"
    assert fn("http://example.com/path#fragment") == "http://example.com/path"
    assert fn("http://example.com/path?query=1#fragment") == "http://example.com/path"
    assert fn("http://example.com/path") == "http://example.com/path"
    assert fn("http://example.com") == "http://example.com"


def test_merge_query_string():
    fn = merge_query_string
    # 시나리오 1: 쿼리가 없는 URL에 파라미터를 추가하는 경우
    url, params = "https://example.com/path", {"a": ["1"], "b": ["hello"]}
    assert fn(url, params) == "https://example.com/path?a=1&b=hello"

    # 시나리오 2: 기존 쿼리에 새로운 키의 파라미터를 추가하는 경우
    url, params = "https://example.com?a=1", {"b": ["2"]}
    assert fn(url, params) == "https://example.com?a=1&b=2"

    # 시나리오 3: overwrite=False일 때, 기존 키에 값을 추가(확장)하는 경우
    url, params = "https://example.com?a=1&b=2", {"a": ["3"], "c": ["4"]}
    assert fn(url, params, overwrite=False) == "https://example.com?a=1&a=3&b=2&c=4"

    # 시나리오 4: overwrite=True일 때, 기존 키의 값을 덮어쓰는 경우
    url, params = "https://example.com?a=1&b=2", {"a": ["new_value"], "c": ["100"]}
    assert fn(url, params, overwrite=True) == "https://example.com?a=new_value&b=2&c=100"

    # 시나리오 5: URL 인코딩이 기본으로 활성화되어 특수문자를 변환하는 경우
    assert fn("https://example.com", {"q": ["a/b c"]}).endswith(f"?{"q=a%2Fb+c"}")

    # 시나리오 6: 빈 파라미터를 전달하면 URL이 변경되지 않는 경우
    assert fn("https://example.com?a=1", {}) == "https://example.com?a=1"

    # 엣지 케이스: 최종 쿼리가 비었을 때 URL 끝에 '?'가 없는지 확인
    assert fn("https://example.com", {}) == "https://example.com"
