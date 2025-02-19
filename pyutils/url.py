from urllib.parse import urlparse


def get_base_url(url: str) -> str:
    parsed_rul = urlparse(url)
    new_path = parsed_rul.path.rsplit("/", 1)[0]
    return f"{parsed_rul.scheme}://{parsed_rul.netloc}{new_path}"


def get_origin_url(url: str) -> str:
    parsed_rul = urlparse(url)
    return f"{parsed_rul.scheme}://{parsed_rul.netloc}"


def get_query_string(url: str) -> str:
    parsed_rul = urlparse(url)
    return parsed_rul.query
