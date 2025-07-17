from pyutils.strings import merge_intersected_strings


def test_merge_intersected_strings():
    fn = merge_intersected_strings
    assert fn("abc", "bcd") == "abcd"
    assert fn("abc", "abc") == "abc"
    assert fn("abc", "def") == "abcdef"
