from pydantic import BaseModel,field_validator,Field
from typing import List


class Hobby(BaseModel):
    detail: str
    name: str


class User(BaseModel):
    name: str 
    age: int = Field(..., gt=0, lt=100, description='用户年龄')
    address: str 
    hobby: List[Hobby]
    
    @field_validator('name')
    def name_is_alpha(cls,value):
        assert value.isalpha(), 'name must be alpha'
        return value
        

