from fastapi import APIRouter
from user.validator import StudentsValidator
from user.validator import StudentsQueryValidator
import asyncio

router = APIRouter(
    prefix="/user",
    tags=['用户中心']
)


@router.get("/")
async def all_students():
    return {"students": 'xixi'}


@router.get("/test")
async def test():
    await asyncio.sleep(5)  # 使用异步的 sleep 函数
    return {"test": "test"}
