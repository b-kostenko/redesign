__all__ = ["logger"]

import logging
import sys
from typing import Any, Protocol

from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8",
    )


class Logger(Protocol):
    def info(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def warn(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def error(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None: ...


class StdLogger(Logger):
    def __init__(self, settings: LoggerSettings) -> None:
        root = logging.getLogger()
        root.setLevel(settings.level)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(settings.level)

        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)

        root.handlers.clear()
        root.addHandler(handler)

        self.logger = logging.getLogger("app")

    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self.logger.info(msg, *args, **kwargs)

    def warn(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self.logger.error(msg, *args, **kwargs)

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self.logger.debug(msg, *args, **kwargs)


logger: Logger = StdLogger(LoggerSettings())
