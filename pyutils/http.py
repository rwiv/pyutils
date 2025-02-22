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


def to_cookie_dict(cookie_string: str) -> list[CookieDict]:
    cookies = cookie_string.strip(";").split("; ")
    result: list[CookieDict] = []
    for pair in cookies:
        name, value = pair.split("=")
        result.append({"name": name, "value": value})
    return result
