from fastapi import APIRouter
from typing import Union, Optional
router = APIRouter(prefix="/user", tags=['用户中心'])


@router.get("/job/{ids}")
async def hello(gl: str, ids: Optional[str] = None, bg: Union[int, None] = None):
    print(gl, ids, bg)
    return {"message": f"Hello user {ids}"}
