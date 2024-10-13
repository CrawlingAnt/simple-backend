from fastapi import HTTPException
from functools import wraps
from fastapi.responses import JSONResponse
from .reponse import APIResponse

class APIException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)
        


def handle_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except APIException as e:
            return JSONResponse(
                status_code=e.status_code,
                content=APIResponse(code=e.status_code, message=str(e.detail)).model_dump()
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content=APIResponse(code=500, message="Internal Server Error").model_dump()
            )
    return wrapper