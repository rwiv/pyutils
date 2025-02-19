from pyutils import error_details, log, stacktrace_details


def test_error_details():
    print()
    try:
        raise Exception("test error")
    except Exception as e:
        log.error(*error_details(e))


def test_stacktrace_details():
    print()
    try:
        raise Exception("test error")
    except:
        log.error(*stacktrace_details())
