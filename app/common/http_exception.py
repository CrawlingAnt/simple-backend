from fastapi import HTTPException
from functools import wraps
from common.reponse import api_response

class APIException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)



def handle_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except APIException as e:
            return api_response(
                message=str(e.detail).model_dump()
            )
        except Exception as e:
            return api_response(
                message=str(e)
            )
    return wrapper