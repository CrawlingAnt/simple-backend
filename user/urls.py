from fastapi import APIRouter
from user.validator import StudentsValidator
from user.validator import StudentsQueryValidator


router = APIRouter(
    prefix="/user",
    tags=['用户中心']
)


@router.post("/")
async def all_students():
    return {"students": 'xixi'}


