from fastapi import APIRouter
from typing import Union, Optional
from user.models import User

router = APIRouter(prefix="/user", tags=['用户中心'])


@router.get("/job/{ids}")
async def hello(gl: str, ids: Optional[str] = None, bg: Union[int, None] = None):
    print(gl, ids, bg)
    return {"message": f"Hello user {ids}"}


@router.post("/add")
async def create_user(user: User):
    print(user.model_dump())
    return user

