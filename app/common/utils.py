import logging
import os
from passlib.context import CryptContext
from logging.handlers import TimedRotatingFileHandler
from fastapi import Request
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=10)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_request_info(request:Request):
    start_time = datetime.now()
    method = request.method
    url = request.url

    return f"{start_time} 收到请求: {method} - {url}"


def init_log():
    # 创建日志目录
    log_directory = 'logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # 设置日志级别

    # 日志级别和对应的文件名
    log_levels = {
        logging.INFO: 'info',
        logging.WARNING: 'warning',
        logging.ERROR: 'error',
        logging.CRITICAL: 'critical'
    }

    # 为每个日志级别创建一个处理器
    for level, level_name in log_levels.items():
        log_file_path = os.path.join(log_directory, f'{level_name}.log')

        # 创建 TimedRotatingFileHandler
        file_handler = TimedRotatingFileHandler(
            log_file_path,
            when='midnight',  # 每天午夜轮换
            interval=1,  # 每 1 个单位轮换一次
            backupCount=30,  # 保留 30 天的日志
            encoding='utf-8'
        )
        file_handler.setLevel(level)

        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)

        # 添加处理器到 logger
        logger.addHandler(file_handler)

    # 创建 StreamHandler 用于控制台输出
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)  # 控制台只输出 INFO 及以上级别的日志
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


logger = init_log()
