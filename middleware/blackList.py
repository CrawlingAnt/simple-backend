from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse


class BlackListMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(request.url.path)
        if request.url.path.startswith("/user"):
            print(request.client.host)
            if request.client.host in ["localhost"]:
                return JSONResponse(status_code=403, content={"detail": "Access forbidden"})

        response = await call_next(request)
        return response
