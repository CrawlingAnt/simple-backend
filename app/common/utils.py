import logging
import os
from passlib.context import CryptContext
from logging.handlers import RotatingFileHandler

pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=10)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def init_log():
    # 创建日志目录
    log_diretory = 'logs'
    if not os.path.exists(log_diretory):
        os.makedirs(log_diretory)

    # 配置日志
    log_file_path = os.path.join(log_diretory, 'app.log')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # 创建日志处理器
    file_handler = RotatingFileHandler(log_file_path, maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(logging.INFO)

    # 创建 StreamHandler 用于控制台输出
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # 添加处理器到 logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

logger = init_log()