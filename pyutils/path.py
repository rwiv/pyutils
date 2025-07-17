import os.path
from pathlib import Path
from typing import Union


def find_project_root() -> Path:
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / ".git").exists():
            return parent
    return current_path


def path_join(*paths: Union[str, int, float, Path, None], delimiter: str = "/") -> str:
    cleaned_paths = []
    for i, rp in enumerate(paths):
        if rp is None:
            continue

        if not isinstance(rp, (str, int, float, Path)):
            raise TypeError(f"Invalid path type: {type(rp)}")

        sp = str(rp)
        if not sp:
            continue
        if isinstance(rp, Path):
            sp = sp.replace(os.path.sep, delimiter)

        if i == 0:
            cleaned_paths.append(sp.rstrip(delimiter))
        elif i == len(paths) - 1:
            cleaned_paths.append(sp.lstrip(delimiter))
        else:
            cleaned_paths.append(sp.strip(delimiter))

    return delimiter.join(cleaned_paths)


def dirpath(file_path: str, delimiter: str = "/") -> str:
    return delimiter.join(split_path(file_path)[:-1])


def filename(file_path: str) -> str:
    return Path(file_path).name


def stem(file_path: str) -> str:
    return Path(file_path).stem


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
