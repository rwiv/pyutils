import sys
import traceback
from typing import Any


def stacktrace():
    exc_info = sys.exc_info()
    trace = traceback.format_exception(*exc_info)
    return "".join(trace)


# e.g. log.error(*stacktrace_details())
def stacktrace_details() -> tuple[str, dict[str, Any]]:
    exc_info = sys.exc_info()
    trace = traceback.format_exception(*exc_info)
    head = trace[len(trace) - 1].replace("\n", "")
    return head, {"stacktrace": "".join(trace)}


# e.g. log.error(*error_details(e))
def error_details(ex: Exception) -> tuple[str, dict[str, Any]]:
    msg = str(ex)
    exc_info = sys.exc_info()
    trace = traceback.format_exception(*exc_info)
    details = {"type": ex.__class__.__name__, "message": msg, "stacktrace": "".join(trace)}
    return msg, details
