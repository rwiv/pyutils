from typing import TypedDict


class CookieDict(TypedDict):
    name: str
    value: str


def cookie_header(cookies: list[CookieDict]) -> str:
    result = ""
    for i, cookie in enumerate(cookies):
        result += f"{cookie['name']}={cookie['value']}"
        if i != len(cookies) - 1:
            result += "; "
    return result
