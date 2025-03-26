import pytest

from pyutils.none import not_none


def test_not_null():
    assert not_none(10) == 10
    assert not_none(None, "Test", 5) == 5
    assert not_none("Hello") == "Hello"
    with pytest.raises(ValueError):
        not_none(None)
