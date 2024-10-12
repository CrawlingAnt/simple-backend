from fastapi import APIRouter, HTTPException, Depends
from user.validator import AddUser,QueryUser
from common.utils import get_password_hash
from settings.orm import engine,get_async_session
from sqlmodel import Session, select
from models.main import User
from common.constant import *
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import asyncio

router = APIRouter(
    prefix="/user",
    tags=['用户中心']
)


@router.post("/")
async def all_students(user: QueryUser):
    with Session(engine) as session:
        filters = user.model_dump(exclude_unset=True, exclude_none=True)
        # 使用 SQLModel 的过滤功能
        query = select(User).filter_by(**filters)
        users = session.exec(query).all()
        return {"users": users}


@router.post("/add")
async def test(users: AddUser, session: AsyncSession = Depends(get_async_session)):
    start = datetime.now()
    tasks = []
    async with session.begin():
        # 检查用户是否存在等逻辑
        tasks.append(asyncio.create_task(process_user(users, session)))
        await asyncio.gather(*tasks)
        return {"message": f"{ start} - {datetime.now()} Users created successfully"}

async def process_user(user: AddUser, session: AsyncSession):
    is_exists = (await session.execute(select(User).where(User.user_name == user.user_name))).scalar_one_or_none()
    if is_exists:
        raise HTTPException(status_code=400, detail=USER_EXISTS)
    hashed_password = get_password_hash(user.password)
    new_user = User(user_name=user.user_name, hashed_password=hashed_password, password=user.password)
    session.add(new_user)

