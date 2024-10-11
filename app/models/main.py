from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional


class UserType(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(description="用户类型", max_length=20)
    status: Optional[int] = Field(description="状态 1 正常 2 禁用",default=1)
    type: Optional[int ]= Field(description="类型 1 管理员 2 普通用户" ,default=2)


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_name: str = Field(description="用户名", max_length=20)
    avatar: Optional[str] = Field(description="头像", max_length=200,default=None)
    email: Optional[str] = Field(description="邮箱", max_length=50,default=None)
    password: str = Field(description="密码", max_length=50)
    hashed_password: str = Field(description="哈希密码", max_length=100)
    description: Optional[str] = Field(description="描述", max_length=200,default=None)
    phone: Optional[str] = Field(description="电话", max_length=11,default=None)
    create_time: datetime = Field(description="创建时间")
    update_time: datetime = Field(description="更新时间")

    user_type: UserType = Relationship(back_populates="users")
    user_type_id: int = Field(description="用户类型id",foreign_key="user_type.id",default=1)


class ArticleLinkCategory(SQLModel, table=True):
    id: int = Field(primary_key=True)
    category_id: int = Field(description="分类id")
    article_id: int = Field(description="文章id")
    create_time: datetime = Field(description="创建时间")
    update_time: datetime = Field(description="更新时间")


class Category(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(description="分类名", max_length=20)
    description: str = Field(description="描述", max_length=200)
    create_time: datetime = Field(description="创建时间")
    update_time: datetime = Field(description="更新时间")
    status: Optional[int] = Field(description="状态 1 正常 2 禁用",default=1)
    articles: list['Article'] = Relationship(back_populates="categories",link_model=ArticleLinkCategory)


class Article(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(description="标题", max_length=200)
    sub_title:Optional[str] = Field(description="副标题", max_length=200,default=None)
    content_json:str = Field(description="内容")
    content_html:str = Field(description="内容")
    create_time: datetime = Field(description="创建时间")
    update_time: datetime = Field(description="更新时间")
    status: Optional[int] = Field(description="状态 1 发布 2 草稿 3 删除 4 禁用",default=2)
    cover: Optional[str] = Field(description="封面", max_length=200,default=None)
    is_top: Optional[int] = Field(description="是否置顶 2 否 1 是",default=2)
    is_recommend: Optional[int] = Field(description="是否推荐 2 否 1 是",default=2)
    is_original: Optional[int] = Field(description="是否原创 2 否 1 是",default=2)
    is_comment: Optional[int] = Field(description="是否评论 2 否 1 是",default=2)
    author: Optional['User'] = Relationship(back_populates="articles")
    author_id: int = Field(description="作者id",foreign_key="user.id")


    categories: list['Category'] = Relationship(back_populates="articles",link_model=ArticleLinkCategory)




