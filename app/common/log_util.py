import logging
from app.models.log import Logs
from app.settings.orm import get_async_session
import asyncio


def pull_logs_to_db(message: str, level="INFO"):
    print('-------', message, level)


class LoggerDbHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        level = record.levelname
        message = record.getMessage()
        pull_logs_to_db(message, level)


def init_db_logger():
    logger_obj = logging.getLogger(__name__)
    logger_obj.setLevel(logging.INFO)
    logger_obj.addHandler(LoggerDbHandler())

    return logger_obj


logger = init_db_logger()
