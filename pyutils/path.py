from pathlib import Path
from typing import Any


def find_project_root():
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / ".git").exists():
            return parent
    return current_path


def path_join(*paths: Any, delimiter: str = "/") -> str:
    cleaned_paths = []
    for i, p in enumerate(paths):
        if not p:
            continue
        p = str(p)
        if i == 0:
            cleaned_paths.append(p.rstrip(delimiter))
        elif i == len(paths) - 1:
            cleaned_paths.append(p.lstrip(delimiter))
        else:
            cleaned_paths.append(p.strip(delimiter))

    return delimiter.join(cleaned_paths)


def dirname(file_path: str, delimiter: str = "/") -> str:
    return delimiter.join(file_path.split(delimiter)[:-1])


def filename(file_path: str, delimiter: str = "/") -> str:
    return file_path.split(delimiter)[-1]


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
