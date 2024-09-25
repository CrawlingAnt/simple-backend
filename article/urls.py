from fastapi import APIRouter

router = APIRouter(
    prefix="/article",
    tags=["article"],
)


@router.get("/")
async def hello():
    return {"message": "Hello World"}
