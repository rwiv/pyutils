import json
import logging
import os
from datetime import datetime
from typing import Any

RESET = "\x1b[0m"
RED_BOLD = "\x1b[1;31m"
GREEN_BOLD = "\x1b[1;32m"
YELLOW_BOLD = "\x1b[1;33m"
BLUE_BOLD = "\x1b[1;34m"
PURPLE_BOLD = "\x1b[1;35m"
CYAN_BOLD = "\x1b[1;36m"
WHITE_BOLD = "\x1b[1;37m"
WHITE_DIMMED = "\x1b[2;37m"
GRAY = "\x1b[90m"

DEBUG = f"{BLUE_BOLD}DEBUG:{RESET}"
INFO = f"{GREEN_BOLD}INFO:{RESET}"
WARN = f"{YELLOW_BOLD}WARN:{RESET}"
ERROR = f"{PURPLE_BOLD}ERROR:{RESET}"
FATAL = f"{RED_BOLD}FATAL:{RESET}"

PROD_ENV = "prod"
ENV_KEY = "PY_ENV"


def get_std_logger(name: str = "app", level: int = logging.INFO):
    std_logger = logging.getLogger(name)
    std_logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter())
    std_logger.addHandler(ch)
    return std_logger


def get_msg_prod(level: str, message: str, attrs: dict[str, Any] | None) -> str:
    record = {
        "level": level,
        "message": message,
        "timestamp": datetime.now().isoformat(),
    }
    if attrs is not None:
        for key, value in attrs.items():
            record[key] = value

    return json.dumps(record)


def get_msg_dev(level: str, msg: str, attrs: dict[str, Any] | None) -> str:
    now = datetime.now()
    formatted_time = now.strftime(f"%H:%M:%S.{now.microsecond // 1000:03d}")

    t = f"{GRAY}[{formatted_time}]{RESET}"
    m = f"{WHITE_BOLD}{msg}{RESET}"
    if attrs is None:
        return f"{t} {level} {m}"
    else:
        a = f"{WHITE_DIMMED}{json.dumps(attrs, indent=2)}{RESET}"
        return f"{t} {level} {m} {a}"


class Logger:
    def __init__(self):
        self.is_prod = os.getenv(ENV_KEY) == PROD_ENV
        self.logger = get_std_logger()

    def set_level(self, level: int = logging.INFO):
        self.logger.setLevel(level)

    def debug(self, msg: str, attrs: dict[str, Any] | None = None):
        if self.is_prod:
            self.logger.debug(get_msg_prod("DEBUG", msg, attrs))
        else:
            self.logger.debug(get_msg_dev(DEBUG, msg, attrs))

    def info(self, msg: str, attrs: dict[str, Any] | None = None):
        if self.is_prod:
            self.logger.info(get_msg_prod("INFO", msg, attrs))
        else:
            self.logger.info(get_msg_dev(INFO, msg, attrs))

    def warn(self, msg: str, attrs: dict[str, Any] | None = None):
        if self.is_prod:
            self.logger.warning(get_msg_prod("WARN", msg, attrs))
        else:
            self.logger.warning(get_msg_dev(WARN, msg, attrs))

    def error(self, msg: str, attrs: dict[str, Any] | None = None):
        if self.is_prod:
            self.logger.error(get_msg_prod("ERROR", msg, attrs))
        else:
            self.logger.error(get_msg_dev(ERROR, msg, attrs))

    def fatal(self, msg: str, attrs: dict[str, Any] | None = None):
        if self.is_prod:
            self.logger.critical(get_msg_prod("FATAL", msg, attrs))
        else:
            self.logger.critical(get_msg_dev(FATAL, msg, attrs))


log = Logger()
