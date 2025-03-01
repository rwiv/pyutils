import re
from urllib.parse import urlparse


def get_base_url(url: str) -> str:
    parsed_rul = urlparse(url)
    new_path = parsed_rul.path.rsplit("/", 1)[0]
    return f"{parsed_rul.scheme}://{parsed_rul.netloc}{new_path}"


def get_origin_url(url: str) -> str:
    parsed_rul = urlparse(url)
    return f"{parsed_rul.scheme}://{parsed_rul.netloc}"


def strip_origin(url: str) -> str:
    parsed_url = urlparse(url)
    path_with_query = parsed_url.path
    if parsed_url.query:
        path_with_query += "?" + parsed_url.query
    if path_with_query == "" or path_with_query == "/":
        raise ValueError(f"Invalid URL: {url}")
    return path_with_query


def get_query_string(url: str) -> str:
    parsed_rul = urlparse(url)
    return parsed_rul.query


def strip_query_string(url: str) -> str:
    return url.split("?")[0]
