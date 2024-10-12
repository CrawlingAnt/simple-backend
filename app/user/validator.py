from pydantic import BaseModel
from typing import Optional


class AddUser(BaseModel):
    user_name: str
    password: str


class QueryUser(BaseModel):
    user_name: Optional[str] = None
    password: Optional[str] = None
    pageSize: Optional[int] = None
    pageNum: Optional[int] = None
