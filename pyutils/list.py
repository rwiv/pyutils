from typing import TypeVar

T = TypeVar("T")


def sublist(lst: list[T], size: int) -> list[list[T]]:
    return [lst[i : i + size] for i in range(0, len(lst), size)]
