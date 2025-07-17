from urllib.parse import urlparse, urlunsplit


def get_base_url(url: str) -> str:
    parsed_url = urlparse(url)
    base_path = parsed_url.path.rsplit("/", 1)[0] or "/"
    return urlunsplit((parsed_url.scheme, parsed_url.netloc, base_path, "", ""))


def get_origin_url(url: str) -> str:
    parsed_url = urlparse(url)
    return urlunsplit((parsed_url.scheme, parsed_url.netloc, "", "", ""))


def strip_origin(url: str, allow_empty: bool = True) -> str:
    parsed_url = urlparse(url)
    full_path = urlunsplit(("", "", parsed_url.path, parsed_url.query, parsed_url.fragment))
    if not allow_empty and (full_path == "" or full_path == "/"):
        raise ValueError(f"Failed to strip origin url: {url}")
    return full_path
