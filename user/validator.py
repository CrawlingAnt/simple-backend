from pydantic import BaseModel
from typing import Optional, Literal, Any

from pydantic.main import IncEx


class StudentsValidator(BaseModel):
    name: str
    pwd: str
    no: str
    Class_id: int


class StudentsQueryValidator(BaseModel):
    name: Optional[str] = None
    no: Optional[str] = None
    Class_id: Optional[int] = None
