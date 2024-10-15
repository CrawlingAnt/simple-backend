from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base
from pydantic import BaseModel
from typing import Optional

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(20), comment="用户名")
    password = Column(String(20), comment="密码")
    hashed_password = Column(String(100), comment="哈希密码")
    avatar = Column(String(200), default=None, comment="头像")
    email = Column(String(50), default=None, comment="邮箱")
    phone = Column(String(11), default=None, comment="电话")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, comment="更新时间")

    user_type_id = Column(Integer, ForeignKey("user_types.id"), comment="用户类型id")
    user_type = relationship("UserType", back_populates="users")
    articles = relationship("Article", back_populates="user")

class UserType(Base):
    __tablename__ = "user_types"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), comment="用户类型")
    status = Column(Integer, default=1, comment="状态 1 正常 2 禁用")
    type = Column(Integer, default=2, comment="类型 1 管理员 2 普通用户")
    users = relationship("User", back_populates="user_type")



class UserCreate(BaseModel):
    user_name: str
    password: str
    avatar: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    id: Optional[int] = None
