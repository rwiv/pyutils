import os


def read_file(file_path: str, encoding: str = "utf-8") -> str:
    with open(file_path, "r", encoding=encoding) as f:
        return f.read()


def read_bfile(file_path: str) -> bytes:
    with open(file_path, "rb") as f:
        return f.read()


def write_file(
    file_path: str,
    data: str | bytes,
    dir_check: bool = True,
    encoding: str = "utf-8",
):
    if dir_check:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if isinstance(data, bytes):
        with open(file_path, "wb") as f:
            f.write(data)
    elif isinstance(data, str):
        with open(file_path, "w", encoding=encoding) as f:
            f.write(data)


def delete_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)


def get_directory_size(directory: str) -> int:
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size
