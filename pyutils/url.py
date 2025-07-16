from urllib.parse import urlparse, parse_qs, urlencode


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
    return urlparse(url).query


def strip_query_string(url: str) -> str:
    return url.replace(f"?{urlparse(url).query}", "")


def to_query_string(params: dict[str, list[str]], url_encode: bool = True) -> str:
    if url_encode:
        return urlencode(params, doseq=True)

    result = ""
    is_first = True
    for key, values in params.items():
        for value in values:
            if not is_first:
                result += "&"
            result += f"{key}={value}"
            if is_first:
                is_first = False
    return result


def parse_query_params(url: str) -> dict[str, list[str]]:
    return parse_qs(urlparse(url).query)
