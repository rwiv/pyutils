from pathlib import Path

import pytest

from pyutils import dirpath, path_join, filename, get_ext


def test_dirname():
    assert dirpath("a\\b/c.txt") == "a/b"


def test_filename():
    assert filename("a/b\\c.txt") == "c.txt"
    print(Path("a\\b/c.txt").parts)


def test_join():
    assert path_join("home", "user", "documents") == "home/user/documents"
    assert path_join("/home/", "/user/", "documents/", delimiter="/") == "/home/user/documents/"


def test_ext():
    assert get_ext("a/b/c.txt") == "txt"
    assert get_ext("a/b/c") is None
    with pytest.raises(ValueError):
        get_ext("a/b/c.")
