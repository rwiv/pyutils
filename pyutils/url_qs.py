from urllib.parse import urlparse, parse_qs, urlencode, urlunsplit


def strip_query_string(url: str) -> str:
    parsed_url = urlparse(url)
    return urlunsplit((parsed_url.scheme, parsed_url.netloc, parsed_url.path, "", ""))


def get_query_string(url: str) -> str:
    return urlparse(url).query


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


def merge_query_string(
    url: str,
    params: dict[str, list[str]],
    overwrite: bool = False,
    url_encode: bool = True,
) -> str:
    new_params = parse_query_params(url)
    for k, v in params.items():
        if overwrite or k not in new_params:
            new_params[k] = v
        else:
            new_params[k].extend(v)
    query_string = to_query_string(params=new_params, url_encode=url_encode)
    if query_string == "":
        return url
    else:
        return f"{strip_query_string(url)}?{query_string}"
