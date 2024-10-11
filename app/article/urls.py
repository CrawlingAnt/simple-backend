from fastapi import APIRouter
from sqlmodel import Session, select
from models.main import UserType
from settings.orm import engine


router = APIRouter(
    prefix="/article",
    tags=["文章列表"],
)


@router.get("/")
async def hello():
    with Session(engine) as session:
        statement = select(UserType)
        result = session.exec(statement).all()

    return {"message": "Hello World", "content": result}


