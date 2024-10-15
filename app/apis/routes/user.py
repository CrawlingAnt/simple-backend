from fastapi import APIRouter, HTTPException, Depends
from common.utils import get_password_hash
from settings.orm import get_async_session
from common.constant import *
from sqlalchemy.ext.asyncio import AsyncSession
from common.reponse import api_response
from common.http_exception import handle_exceptions

user_router = APIRouter()


@user_router.post("/")
@handle_exceptions
async def all_students():
    return api_response(data='Hello World')


# @user_router.post("/add")
# async def test(user: AddUser, session: AsyncSession = Depends(get_async_session)):
#     is_exists = await session.execute(select(User).where(User.user_name == user.user_name))
#     is_exists = is_exists.scalar_one_or_none()
#     if is_exists:
#         raise HTTPException(status_code=400, detail=USER_EXISTS)
#     new_user = User(user_name=user.user_name, hashed_password=get_password_hash(user.password), password=user.password)
#     try:
#         session.add(new_user)
#         await session.commit()
#         return  api_response(message="User created successfully")
#     except Exception as e:
#         await session.rollback()
#         raise HTTPException(status_code=500, detail=str(e))