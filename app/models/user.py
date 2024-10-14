from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .article import Article


class UserType(SQLModel, table=True):
    __tablename__ = "user_types"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(description="用户类型", max_length=20)
    status: int = Field(description="状态 1 正常 2 禁用", default=1)
    type: int = Field(description="类型 1 管理员 2 普通用户", default=2)
    users: List["User"] = Relationship(back_populates="user_type")


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_name: str = Field(description="用户名", max_length=20, unique=True)
    avatar: Optional[str] = Field(default=None, description="头像", max_length=200)
    email: Optional[str] = Field(default=None, description="邮箱", max_length=50)
    password: str = Field(description="密码", max_length=50)
    hashed_password: str = Field(description="哈希密码", max_length=100)
    description: Optional[str] = Field(default=None, description="描述", max_length=200)
    phone: Optional[str] = Field(default=None, description="电话", max_length=11)
    create_time: datetime = Field(default_factory=datetime.now, description="创建时间")
    update_time: datetime = Field(default_factory=datetime.now, description="更新时间")

    user_type: Optional[UserType] = Relationship(back_populates="users")
    user_type_id: Optional[int] = Field(default=1, foreign_key="user_types.id")

    articles: List["Article"] = Relationship(back_populates="author")
