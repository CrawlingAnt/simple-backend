from fastapi import APIRouter

router = APIRouter(
    prefix="/article",
    tags=["文章列表"],
)


@router.get("/")
async def hello():
    return {"message": "Hello World"}


