from fastapi import APIRouter
from sqlmodel import Session, select
from settings.orm import engine
from .validator import AddArticle

router = APIRouter(
    prefix="/article",
    tags=["文章列表"],
)


@router.get("/")
async def hello():
        
    return {"message": "Hello World", "content": ''}


@router.post('/add')
async def add_article(data: AddArticle):
    # with Session(engine) as session:
    #     user = session.exec(select(User).where(User.id == data.author_id)).first()
    #     if not user:
    #         raise HTTPException(status_code=404, detail="用户不存在")

    print(data)
    pass
