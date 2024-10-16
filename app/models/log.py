from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime


class Logs(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    level = Column(String(20), comment="日志级别 INFO WARN ERROR")
    message = Column(String(200), comment="日志信息")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
