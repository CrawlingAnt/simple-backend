from fastapi import APIRouter, HTTPException
from user.validator import AddUser,QueryUser
from common.utils import get_password_hash
from settings.orm import engine
from sqlmodel import Session, select
from models.main import User
from common.constant import *


router = APIRouter(
    prefix="/user",
    tags=['用户中心']
)


@router.post("/")
async def all_students(user: QueryUser):
    print(user.pageSize)
    with Session(engine) as session:
        filters = user.model_dump(exclude_unset=True, exclude_none=True)
        # 使用 SQLModel 的过滤功能
        query = select(User).filter_by(**filters)
        users = session.exec(query).all()
        return {"users": users}


@router.post("/add")
async def test(user: AddUser):
    with Session(engine) as session:
        is_exists = session.exec(select(User).where(User.user_name == user.user_name)).first()
        if is_exists:
            raise HTTPException(status_code=400, detail=USER_EXISTS)
        user = User(user_name=user.user_name, hashed_password=get_password_hash(user.password),password=user.password)
        try:
            session.add(user)
            session.commit()
            return {"message": "User created successfully"}

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
