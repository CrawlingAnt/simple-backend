from pydantic import BaseModel


class StudentsValidator(BaseModel):
    name: str
    pwd: str
    no: str
    Class_id: int
