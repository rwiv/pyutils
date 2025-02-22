from pyutils.http import to_cookie_dict


def test_to_cookie_dict():
    cookie_string = "a=1; b=2; c=3;"
    cookies = to_cookie_dict(cookie_string)
    assert cookies == [
        {"name": "a", "value": "1"},
        {"name": "b", "value": "2"},
        {"name": "c", "value": "3"},
    ]
