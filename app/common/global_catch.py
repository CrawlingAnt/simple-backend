from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from common.reponse import APIResponse


async def general_exception_handler(request: Request, exc: Exception):  
    print('--------------------', request.url)
    return JSONResponse(
        status_code=500,
        content=APIResponse(code=500, message="Internal Server Error", data={"detail": str(exc)}).dict()
    )



def init_global_exception_handler(app: FastAPI):
    app.add_exception_handler(Exception, general_exception_handler) 
