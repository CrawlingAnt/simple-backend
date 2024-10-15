from fastapi import APIRouter
from .routes import user, article


api_router = APIRouter()
api_router.include_router(user.user_router, prefix="/users", tags=["用户中心"])
api_router.include_router(article.article_router, prefix="/articles", tags=["文章中心"])