from pathlib import Path
from typing import Any, Union


def find_project_root():
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / ".git").exists():
            return parent
    return current_path


def path_join(*paths: Union[str, int, float, None], delimiter: str = "/") -> str:
    cleaned_paths = []
    for i, p in enumerate(paths):
        if p is None:
            continue

        if not isinstance(p, (str, int, float)):
            raise TypeError(f"Invalid path type: {type(p)}")

        p = str(p)
        if not p:
            continue

        if i == 0:
            cleaned_paths.append(p.rstrip(delimiter))
        elif i == len(paths) - 1:
            cleaned_paths.append(p.lstrip(delimiter))
        else:
            cleaned_paths.append(p.strip(delimiter))

    return delimiter.join(cleaned_paths)


def dirpath(file_path: str, delimiter: str = "/") -> str:
    return delimiter.join(split_path(file_path)[:-1])


def filename(file_path: str) -> str:
    return Path(file_path).name


def split_path(path: str) -> tuple[str, ...]:
    return Path(path).parts


def get_ext(file_path: str) -> str | None:
    chunks = file_path.split(".")
    if len(chunks) == 1:
        return None
    if chunks[-1] == "":
        raise ValueError("Invalid file path")
    return chunks[-1]


def sanitize_filename(file_name: str) -> str:
    return (
        file_name.replace("?", "？")
        .replace("/", "／")
        .replace("\\", "＼")
        .replace(":", "：")
        .replace("*", "＊")
        .replace('"', "＂")
        .replace("|", "｜")
        .replace(">", "＞")
        .replace("<", "＜")
        .strip()
    )
