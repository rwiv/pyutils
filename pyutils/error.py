import sys
import traceback
from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class ErrorDetails:
    type: str
    message: str
    stacktrace: str
    

def stacktrace() -> str:
    exc_info = sys.exc_info()
    trace = traceback.format_exception(*exc_info)
    return "".join(trace)


def stacktrace_details() -> ErrorDetails:
    exc_info = sys.exc_info()
    trace = traceback.format_exception(*exc_info)
    head = trace[len(trace) - 1].replace("\n", "")
    err_type, message = split_once(head, ":")
    return ErrorDetails(err_type, message, "".join(trace))


def split_once(s: str, delimiter: str = ":"):
    parts = s.split(delimiter, 1)
    if len(parts) == 1:
        return "", s
    return parts[0].strip(), parts[1].strip()


# e.g. log.error(*stacktrace_details())
def stacktrace_entry() -> tuple[str, dict[str, Any]]:
    details = stacktrace_details()
    return details.message, asdict(details)


def error_details(ex: Exception) -> ErrorDetails:
    message = str(ex)
    exc_info = sys.exc_info()
    trace = traceback.format_exception(*exc_info)
    return ErrorDetails(ex.__class__.__name__, message, "".join(trace))


# e.g. log.error(*error_details(e))
def error_entry(ex: Exception) -> tuple[str, dict[str, Any]]:
    details = error_details(ex)
    return details.message, asdict(details)
