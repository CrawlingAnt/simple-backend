from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), comment="分类名")
    description = Column(String(100), default=None, comment="描述")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, comment="更新时间")
    status = Column(Integer, default=1, comment="状态 1 正常 2 禁用")

    articles = relationship("Article", back_populates="category")
