from pydantic import BaseModel
from fastapi import status
from typing import Optional, Any
from fastapi.responses import JSONResponse
from common.utils import object_as_dict

class APIResponse(BaseModel):
    code: int
    message: str
    data: Optional[Any] = None


def api_response(code: int = status.HTTP_200_OK, message: str = "success", data: Optional[Any] = None):
    if isinstance(data, list):
        # 如果是sqlalchemy模型，则转换为字典
        converted_data = [object_as_dict(item)  for item in data]
    else:
        converted_data = data
    return JSONResponse(status_code=code, content={"message": message, "data": converted_data})