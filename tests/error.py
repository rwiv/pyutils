from pyutils import error_entry, log, stacktrace_entry, split_once


def test_error_details():
    print()
    try:
        raise Exception("test error")
    except Exception as e:
        log.error(*error_entry(e))


def test_stacktrace_details():
    print()
    try:
        raise Exception("test error")
    except:
        log.error(*stacktrace_entry())


def test_split_once():
    assert split_once("a:b:c") == ("a", "b:c")
    assert split_once("a:b:c:d") == ("a", "b:c:d")
    assert split_once("a:     b   ") == ("a", "b")
    assert split_once("a") == ("", "a")
    assert split_once("a:") == ("a", "")
    assert split_once(":a") == ("", "a")
    assert split_once("a#b#c", "#") == ("a", "b#c")
