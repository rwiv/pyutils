from typing import TypeVar


T = TypeVar("T")


def not_none(
    value: T | None,
    key_name: str = "Value",
    default: T | None = None,
) -> T:
    if value is not None:
        return value

    if default is not None:
        return default
    else:
        raise ValueError(f"{key_name} is None")
