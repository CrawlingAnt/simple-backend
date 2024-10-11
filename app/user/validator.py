from pydantic import BaseModel


class AddUser(BaseModel):
    user_name: str
    password: str