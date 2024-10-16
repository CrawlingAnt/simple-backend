from fastapi import Request, Response
from fastapi.responses import StreamingResponse
from datetime import datetime
import json
from app.common.log_util import logger


async def log_request(request: Request, call_next):
    no_log_path = ["docs", "openapi.json"]
    query_path = request.url.path.split("/")[1]
    response = await call_next(request)

    if query_path in no_log_path:
        return response

    start_time = datetime.now()
    request_data = {}
    if request.method == "POST":
        request_data = await request.json()
    # 获取表单数据
    if request.headers.get("Content-Type") == "application/x-www-form-urlencoded":
        request_data = await request.form()

    logger.info(f"{start_time} 收到请求: {request.method} {request.url} {request_data}")

    end_time = datetime.now()
    # 处理流式响应
    if isinstance(response, StreamingResponse):
        logger.info(f"{end_time} 返回流式响应耗时: {end_time - start_time}")
        return response

    # 获取响应体
    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk

    # 尝试解析响应体
    try:
        response_data = json.loads(response_body)
    except json.JSONDecodeError:
        response_data = response_body.decode('utf-8')

    logger.info(f"{end_time} 返回响应: {response_data} 耗时: {end_time - start_time}")

    # 重建响应
    return Response(
        content=response_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )


def init_log_request_middleware(app):
    app.middleware("http")(log_request)
