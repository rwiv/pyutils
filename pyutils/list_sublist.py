from typing import TypeVar

T = TypeVar("T")


def sublist(lst: list[T], size: int) -> list[list[T]]:
    if size <= 0:
        raise ValueError("n should be greater than 0")

    result = []
    current = []

    for elem in lst:
        if len(current) >= size:
            result.append(current)
            current = []
        current.append(elem)

    if current:
        result.append(current)

    return result


def sublist_with_idx(lst: list[T], size: int) -> list[list[tuple[int, T]]]:
    if size <= 0:
        raise ValueError("n should be greater than 0")

    result = []
    current = []
    cnt = 0

    for elem in lst:
        if len(current) >= size:
            result.append(current)
            current = []
        current.append((cnt, elem))
        cnt += 1

    if current:
        result.append(current)

    return result


def sublist_n_parts(lst: list[T], num: int) -> list[list[T]]:
    if num <= 0:
        raise ValueError("num should be greater than 0")

    n = len(lst)
    base_size = n // num
    extra = n % num

    result = []
    start = 0

    for i in range(num):
        end = start + base_size + (1 if i < extra else 0)
        result.append(lst[start:end])
        start = end
    return result
