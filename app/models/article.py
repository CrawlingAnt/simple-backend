from sqlmodel import SQLModel, Field, Relationship, Column, Text
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from .many_to_many import ArticleLinkCategory

if TYPE_CHECKING:
    from .user import User


class Article(SQLModel, table=True):
    __tablename__ = "articles"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(description="标题", max_length=200)
    sub_title: Optional[str] = Field(default=None, description="副标题", max_length=200)
    content_json: str = Column(Text, comment="内容json")
    content_html: str = Column(Text, comment="内容html")
    create_time: datetime = Field(default_factory=datetime.now, description="创建时间")
    update_time: datetime = Field(default_factory=datetime.now, description="更新时间")
    status: int = Field(default=2, description="状态 1 发布 2 草稿 3 删除 4 禁用")
    cover: Optional[str] = Field(default=None, description="封面", max_length=200)
    is_top: int = Field(default=2, description="是否置顶 2 否 1 是")
    is_recommend: int = Field(default=2, description="是否推荐 2 否 1 是")
    is_original: int = Field(default=2, description="是否原创 2 否 1 是")
    is_comment: int = Field(default=2, description="是否评论 2 否 1 是")
    author: Optional["User"] = Relationship(back_populates="articles")
    author_id: Optional[int] = Field(default=None, foreign_key="users.id")

    categories: List["Category"] = Relationship(back_populates="articles", link_model=ArticleLinkCategory)


class Category(SQLModel, table=True):
    __tablename__ = "categories"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(description="分类名", max_length=20)
    description: str = Field(description="描述", max_length=100)
    create_time: datetime = Field(default_factory=datetime.now, description="创建时间")
    update_time: datetime = Field(default_factory=datetime.now, description="更新时间")
    status: int = Field(default=1, description="状态 1 正常 2 禁用")
    articles: List[Article] = Relationship(back_populates="categories", link_model=ArticleLinkCategory)
