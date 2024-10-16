import os
from passlib.context import CryptContext
from fastapi import Request
from datetime import datetime
from dotenv import load_dotenv
from pydantic import MySQLDsn
from sqlalchemy.orm import class_mapper

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=10)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_request_info(request: Request):
    start_time = datetime.now()
    method = request.method
    url = request.url

    return f"{start_time} 收到请求: {method} - {url}"


def get_db_url():
    db_url_str: MySQLDsn = MySQLDsn.build(
        scheme=os.getenv("DB_SCHEME"),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        path=os.getenv("DB_NAME"),
    )

    pool_size_num = int(os.getenv("DB_POOL_SIZE"))
    max_overflow_num = int(os.getenv("DB_MAX_OVERFLOW"))

    return db_url_str.unicode_string(), pool_size_num, max_overflow_num


# 将sqlalchemy模型转换为字典
def object_as_dict(obj):
    def convert_datetime(value):
        if isinstance(value, datetime):
            return value.isoformat()
        return value

    return {c.key: convert_datetime(getattr(obj, c.key))
            for c in class_mapper(obj.__class__).columns}


db_url, pool_size, max_overflow = get_db_url()
