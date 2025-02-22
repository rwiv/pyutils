from typing import TypeVar, Callable

T = TypeVar("T")


def find_elem[T](lst: list, cond: Callable[[T], bool]) -> T | None:
    for item in lst:
        if cond(item):
            return item
    return None
