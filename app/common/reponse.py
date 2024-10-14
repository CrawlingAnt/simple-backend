from pydantic import BaseModel
from fastapi import status
from typing import Optional, Any

class APIResponse(BaseModel):
    code: int
    message: str
    data: Optional[Any] = None


def api_response(code: int = status.HTTP_200_OK, message: str = "success", data: Optional[Any] = None):
    return APIResponse(code=code, message=message, data=data)