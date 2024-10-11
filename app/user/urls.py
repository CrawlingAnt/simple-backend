from fastapi import APIRouter, HTTPException
from user.validator import AddUser
from common.utils import get_password_hash
from settings.orm import engine
from sqlmodel import Session, select
from models.main import User
from common.constant import *

router = APIRouter(
    prefix="/user",
    tags=['用户中心']
)


@router.get("/")
async def all_students():
    return {"students": 'xixi'}


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
