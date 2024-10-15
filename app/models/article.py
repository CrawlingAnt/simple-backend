from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), comment="标题")
    sub_title = Column(String(200), default=None, comment="副标题")
    content_json = Column(Text, default=None, comment="内容json")
    content_html = Column(Text, default=None, comment="内容html")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, comment="更新时间")
    status = Column(Integer, default=2, comment="状态 1 发布 2 草稿 3 删除 4 禁用")
    cover = Column(String(200), default=None, comment="封面")
    is_top = Column(Integer, default=2, comment="是否置顶 2 否 1 是")
    is_recommend = Column(Integer, default=2, comment="是否推荐 2 否 1 是")
    is_original = Column(Integer, default=2, comment="是否原创 2 否 1 是")
    is_comment = Column(Integer, default=2, comment="是否评论 2 否 1 是")

    user_id = Column(Integer, ForeignKey("users.id"), comment="用户id")
    user = relationship("User", back_populates="articles")
    category_id = Column(Integer, ForeignKey("categories.id"), comment="分类id")
    category = relationship("Category", back_populates="articles")
