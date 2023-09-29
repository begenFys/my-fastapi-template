import logging
import logging.handlers
from logging import Handler, Formatter, Logger
from typing import Union, NoReturn
from datetime import datetime
import os

# from src.config import PATH_LOG


class AdvLogger:
    """Логирование работы программы"""

    def __init__(self, logger_name: str):
        self.logger: Logger = logging.getLogger(logger_name)
        message_format: str = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        formatter: Formatter = logging.Formatter(message_format)
        self.logger.setLevel(logging.DEBUG)

        stream_handler: Handler = self.init_handler(handler_class=logging.StreamHandler(),
                                                    formatter=formatter,
                                                    level=logging.DEBUG)

        current_date = datetime.now().strftime("%Y_%m_%d")
        # log_filename = os.path.join(PATH_LOG, f"log_{current_date}.log")
        # file_handler: Handler = self.init_handler(
        #     handler_class=logging.handlers.RotatingFileHandler(
        #         filename=log_filename,
        #         maxBytes=1048576,
        #         backupCount=5
        #     ),
        #     formatter=formatter,
        #     level=logging.INFO)

        self.logger.addHandler(stream_handler)
        # self.logger.addHandler(file_handler)
        self.logger.debug("logger init")

    def init_handler(self, handler_class: Handler, formatter: Formatter, level: int) -> Handler:
        handler = handler_class
        handler.setFormatter(formatter)
        handler.setLevel(level)
        return handler

    def write_log(self, level: Union[str, int], msg: str) -> NoReturn:
        self.logger.log(level=eval(f"logging.{level}"), msg=msg)