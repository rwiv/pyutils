from pyutils import find_elem


def test_find_elem():
    assert find_elem([1, 2, 3], lambda x: x == 2) == 2
    assert find_elem([1, 2, 3], lambda x: x == 4) is None

    def cond(x: int) -> bool:
        return x == 3

    assert find_elem([1, 2, 3], cond) == 3
