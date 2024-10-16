import logging
import os
from logging.handlers import TimedRotatingFileHandler


def init_log():
    # 创建日志目录
    log_directory = 'logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logger_object = logging.getLogger(__name__)
    logger_object.setLevel(logging.INFO)  # 设置日志级别
    stream_handler = logging.StreamHandler()

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
        logger_object.addHandler(file_handler)
        stream_handler.setFormatter(formatter)

    # 创建 StreamHandler 用于控制台输出
    stream_handler.setLevel(logging.INFO)  # 控制台只输出 INFO 及以上级别的日志
    logger_object.addHandler(stream_handler)

    return logger_object


logger = init_log()
