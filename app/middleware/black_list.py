from fastapi import Request
from fastapi.responses import JSONResponse

async def black_list_middleware(request:Request,call_next):
    black_list = [""]
    if request.client.host in black_list:
        return JSONResponse(status_code=403, content={"message": "Forbidden"})
    return await call_next(request)


def init_black_list_middleware(app):
    app.middleware("http")(black_list_middleware)