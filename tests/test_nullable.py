import pytest

from pyutils.nullable import not_null


def test_not_null():
    assert not_null(10) == 10
    assert not_null(None, "Test", 5) == 5
    assert not_null("Hello") == "Hello"
    with pytest.raises(ValueError):
        not_null(None)
