from pyutils import dirname, path_join, filename, get_ext


def test_dirname():
    assert dirname("a/b/c.txt") == "a/b"


def test_filename():
    assert filename("a/b/c.txt") == "c.txt"


def test_join():
    assert path_join("home", "user", "documents") == "home/user/documents"
    assert path_join("/home/", "/user/", "documents/", delimiter="/") == "/home/user/documents/"


def test_ext():
    assert get_ext("a/b/c.txt") == "txt"
    assert get_ext("a/b/c") == ""
    assert get_ext("a/b/c.") == ""
