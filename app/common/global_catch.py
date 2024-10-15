from fastapi import Request, FastAPI
from common.utils import logger
from common.utils import get_request_info
from fastapi.responses import JSONResponse


async def general_exception_handler(request: Request, exc: Exception):
    text = get_request_info(request)
    logger.error(f"{text} -  {str(exc)}")
    return JSONResponse(status_code=500, content={"message": str(exc)})



def init_global_exception_handler(app: FastAPI):
    app.add_exception_handler(Exception, general_exception_handler)
