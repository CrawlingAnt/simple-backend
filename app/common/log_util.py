import logging
from app.models.log import Logs
from app.settings.orm import async_session_factory
import asyncio


async def pull_logs_to_db(message: str, level="INFO"):
    async with async_session_factory() as session:
        log_entry = Logs(level=level, message=message)
        session.add(log_entry)
        await session.commit()


class LoggerDbHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.loop = None

    def emit(self, record):
        level = record.levelname
        message = record.getMessage()

        # 如果没有运行中的事件循环，创建一个
        if self.loop is None:
            try:
                self.loop = asyncio.get_running_loop()
            except RuntimeError:
                # 如果没有运行中的事件循环，创建一个新的
                self.loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self.loop)

        asyncio.run_coroutine_threadsafe(pull_logs_to_db(message, level), self.loop)


def init_db_logger():
    logger_obj = logging.getLogger(__name__)
    logger_obj.setLevel(logging.INFO)
    handler = LoggerDbHandler()
    logger_obj.addHandler(handler)
    print("Database logger initialized")  # 调试信息
    return logger_obj


logger = init_db_logger()
