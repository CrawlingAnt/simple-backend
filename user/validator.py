from pydantic import BaseModel
from typing import Optional, List


class StudentsValidator(BaseModel):
    name: str
    pwd: str
    no: str
    Class_id: int
    course_id: List[int]


class StudentsQueryValidator(BaseModel):
    name: Optional[str] = None
    no: Optional[str] = None
    Class_id: Optional[int] = None
