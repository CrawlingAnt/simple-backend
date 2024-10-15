from fastapi import APIRouter, HTTPException, Depends
from app.common.utils import get_password_hash
from app.settings.orm import get_async_session
from app.common.constant import *
from sqlalchemy.ext.asyncio import AsyncSession
from app.common.reponse import api_response
from app.models.user import User, UserCreate
from sqlalchemy.future import select
from sqlalchemy.sql.expression import literal

user_router = APIRouter()


@user_router.get("/")
async def all_students(session: AsyncSession = Depends(get_async_session)):
    stmt = await session.execute(select(User))
    data = stmt.scalars().all()
    return api_response(data=data)


@user_router.post("/add")
async def test(user: UserCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = await session.execute(select(User).where(User.user_name == literal(user.user_name)))
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
        raise api_response(code=500, data=str(e))
