from pathlib import Path

import pytest

from pyutils import dirpath, path_join, filename, get_ext


def test_dirname():
    assert dirpath("a\\b/c.txt") == "a/b"


def test_filename():
    assert filename("a/b\\c.txt") == "c.txt"
    print(Path("a\\b/c.txt").parts)


def test_ext():
    assert get_ext("a/b/c.txt") == "txt"
    assert get_ext("a/b/c") is None
    with pytest.raises(ValueError):
        get_ext("a/b/c.")


# 기본 케이스 테스트: 여러 문자열 경로를 기본 구분자("/")로 연결
def test_path_join():
    fn = path_join
    # 기본 케이스
    assert fn("home", "user", "documents") == "home/user/documents"

    # 앞, 뒤에 구분자가 있는 경우
    assert fn("/home/", "/user/", "documents/", delimiter="/") == "/home/user/documents/"

    # 단일 인자 테스트: 경로 조각이 하나만 있을 경우
    assert fn("one_path") == "one_path"
    assert fn(123) == "123"

    # 인자가 없는 엣지 케이스 테스트
    assert fn() == ""

    # 다양한 자료형(str, int, float) 혼합 테스트
    assert fn("path", 1, "to", 2.5, "file") == "path/1/to/2.5/file"
    assert fn(2025, "year", 7, 17.0) == "2025/year/7/17.0"

    # 사용자 지정 구분자 테스트
    assert fn("a", "b", "c", delimiter="-") == "a-b-c"
    assert fn("a", "b", "c", delimiter="--->") == "a--->b--->c"
    assert fn("a", "b", delimiter=" ") == "a b"

    # 빈 문자열 구분자 엣지 케이스 테스트
    assert fn("a", "b", "c", delimiter="") == "abc"

    # 경로 조각에 빈 문자열이 포함된 엣지 케이스 테스트
    assert fn("a", "", "c") == "a/c"
    assert fn("a", None, "c") == "a/c"
    assert fn("", "start") == "start"
    assert fn("end", "") == "end"

    # 경로 조각이 이미 구분자를 포함하고 있는 엣지 케이스 테스트
    assert fn("a/b", "c", "d") == "a/b/c/d"
    assert fn("a-b", "c", delimiter="-") == "a-b-c"

    # 특수문자 및 공백 포함 경로 테스트
    assert fn("file name with spaces", "folder@1") == "file name with spaces/folder@1"

    # 어노테이션에 명시되지 않은 타입(None, list) 테스트
    with pytest.raises(TypeError):
        fn("a", [1, 2], "c")  # type: ignore

    # 숫자로만 이루어진 경로 테스트
    assert fn(2025, 7, 17) == "2025/7/17"
    assert fn(3.14, 1.618, delimiter=":") == "3.14:1.618"
