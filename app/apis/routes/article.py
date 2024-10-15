from fastapi import APIRouter, Depends
from common.reponse import api_response
from settings.orm import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.article import Article

article_router = APIRouter()

@article_router.get("/")
async def all_articles(session: AsyncSession = Depends(get_async_session)):
    stmt = await session.execute(select(Article))
    data = stmt.scalars().all()
    return api_response(data=data)

