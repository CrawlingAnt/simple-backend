from fastapi import APIRouter, HTTPException, Depends
from common.utils import get_password_hash
from settings.orm import get_async_session
from common.constant import *
from sqlalchemy.ext.asyncio import AsyncSession
from common.reponse import api_response
from models.user import User, UserCreate
from sqlalchemy.future import select


user_router = APIRouter()


@user_router.get("/")
async def all_students(session: AsyncSession = Depends(get_async_session)):
    stmt = await session.execute(select(User))
    data = stmt.scalars().all()
    return api_response(data=data)

@user_router.post("/add")
async def test(user: UserCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = await session.execute(select(User).where(User.user_name == user.user_name))
    if stmt.scalar_one_or_none():
        raise HTTPException(status_code=400, detail=USER_EXISTS)
    hashed_password = get_password_hash(user.password)
    new_user = User(**user.model_dump(), hashed_password=hashed_password)
    try:
        session.add(new_user)
        await session.commit()
        return api_response(message="用户创建成功")
    except Exception as e:
        await session.rollback()
        raise api_response(status_code=500, detail=str(e))
