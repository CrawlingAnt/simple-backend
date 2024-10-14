from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class ArticleLinkCategory(SQLModel, table=True):
    __tablename__ = "article_link_category"
    id: Optional[int] = Field(default=None, primary_key=True)
    category_id: int = Field(foreign_key="categories.id")
    article_id: int = Field(foreign_key="articles.id")
    create_time: datetime = Field(default_factory=datetime.now, description="创建时间")
    update_time: datetime = Field(default_factory=datetime.now, description="更新时间")
