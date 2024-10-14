from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import Text
from datetime import datetime
from typing import Optional, List, ForwardRef


class UserType(SQLModel, table=True):
    __tablename__ = "usertype"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(description="用户类型", max_length=20)
    status: int = Field(description="状态 1 正常 2 禁用", default=1)
    type: int = Field(description="类型 1 管理员 2 普通用户", default=2)
    users: List["User"] = Relationship(back_populates="user_type")


class User(SQLModel, table=True):
    __tablename__ = "user"
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
    user_type_id: Optional[int] = Field(default=1, foreign_key="usertype.id")

    articles: List["Article"] = Relationship(back_populates="author")


class ArticleLinkCategory(SQLModel, table=True):
    __tablename__ = "article_link_category"
    id: Optional[int] = Field(default=None, primary_key=True)
    category_id: int = Field(foreign_key="category.id")
    article_id: int = Field(foreign_key="article.id")
    create_time: datetime = Field(default_factory=datetime.now, description="创建时间")
    update_time: datetime = Field(default_factory=datetime.now, description="更新时间")


class Category(SQLModel, table=True):
    __tablename__ = "category"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(description="分类名", max_length=20)
    description: str = Field(description="描述", max_length=200)
    create_time: datetime = Field(default_factory=datetime.now, description="创建时间")
    update_time: datetime = Field(default_factory=datetime.now, description="更新时间")
    status: int = Field(default=1, description="状态 1 正常 2 禁用")
    articles: List["article"] = Relationship(back_populates="categories", link_model=ArticleLinkCategory)


article = ForwardRef("Article")


class Article(SQLModel, table=True):
    __tablename__ = "article"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(description="标题", max_length=200)
    sub_title: Optional[str] = Field(default=None, description="副标题", max_length=200)
    content_json: str = Column(sa_column=Text, comment="内容json")
    content_html: str = Column(sa_column=Text, comment="内容html")
    create_time: datetime = Field(default_factory=datetime.now, description="创建时间")
    update_time: datetime = Field(default_factory=datetime.now, description="更新时间")
    status: int = Field(default=2, description="状态 1 发布 2 草稿 3 删除 4 禁用")
    cover: Optional[str] = Field(default=None, description="封面", max_length=200)
    is_top: int = Field(default=2, description="是否置顶 2 否 1 是")
    is_recommend: int = Field(default=2, description="是否推荐 2 否 1 是")
    is_original: int = Field(default=2, description="是否原创 2 否 1 是")
    is_comment: int = Field(default=2, description="是否评论 2 否 1 是")
    author: Optional[User] = Relationship(back_populates="articles")
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")

    categories: List[Category] = Relationship(back_populates="articles", link_model=ArticleLinkCategory)


Article.model_rebuild()
