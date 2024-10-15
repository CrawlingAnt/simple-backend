from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from middleware import init_middleware
from common.global_catch import init_global_exception_handler
import os
from dotenv import load_dotenv
from apis.main import api_router

load_dotenv()
app = FastAPI()
app.mount('/static', StaticFiles(directory='assets'), name='static')
app.include_router(api_router)

init_global_exception_handler(app)
# 加载中间件
init_middleware(app)


if __name__ == "__main__":
    uvicorn.run(os.getenv("APP_NAME"), host=os.getenv("HOST"), port=int(os.getenv("PORT")), reload=os.getenv("RELOAD") == "True")
