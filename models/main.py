from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class UserType(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(description="用户类型", max_length=20)
    status: int = Field(description="状态") # 0 正常 1 禁用
    type: int = Field(description="类型") # 0 管理员 1 用户


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_name: str = Field(description="用户名", max_length=20)
    avatar: str = Field(description="头像", max_length=200)
    email: str = Field(description="邮箱", max_length=50)
    password: str = Field(description="密码", max_length=50)
    hashed_password: str = Field(description="哈希密码", max_length=100)
    description: str = Field(description="描述", max_length=200)
    phone: str = Field(description="电话", max_length=11)
    create_time: datetime = Field(description="创建时间")
    update_time: datetime = Field(description="更新时间")

    user_type: UserType = Relationship(description="用户类型",back_populates="users")


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

    articles: list['Article'] = Relationship(description="文章",back_populates="categories",link_model=ArticleLinkCategory)


class Article(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(description="标题", max_length=200)
    sub_title:str = Field(description="副标题", max_length=200)
    content_json:str = Field(description="内容", max_length=10000)
    content_html:str = Field(description="内容", max_length=10000)
    create_time: datetime = Field(description="创建时间")
    update_time: datetime = Field(description="更新时间")
    author: User = Relationship(description="作者",back_populates="articles")
    status: int = Field(description="状态") # 1 发布 2 草稿 3 删除 4 禁用
    tags: str = Field(description="标签", max_length=200)
    cover: str = Field(description="封面", max_length=200)
    is_top: int = Field(description="是否置顶") # 0 否 1 是
    is_recommend: int = Field(description="是否推荐") # 0 否 1 是
    is_original: int = Field(description="是否原创") # 0 否 1 是
    is_comment: int = Field(description="是否评论") # 0 否 1 是

    categories: list['Category'] = Relationship(description="分类",back_populates="articles",link_model=ArticleLinkCategory)




