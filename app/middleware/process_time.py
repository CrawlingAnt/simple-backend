import time
from fastapi import Request, Response

async def add_process_time(request: Request, next_call):
    start_time = time.time()
    response: Response = await next_call(request)
    response.headers["X-Process-Time"] = str(time.time() - start_time)
    return response

async def log_request(request: Request, next_call):
    print(f"Received request: {request.method} {request.url}")
    response = await next_call(request)
    print(f"Sent response: {response.status_code}")
    return response

