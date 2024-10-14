from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import user.urls as user_urls
import article.urls as article_urls
import uvicorn
from middleware import init_middleware
from common.global_catch import init_global_exception_handler
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.mount('/static', StaticFiles(directory='assets'), name='static')


init_global_exception_handler(app)
# 加载中间件
init_middleware(app)

app.include_router(user_urls.router)
app.include_router(article_urls.router)

if __name__ == "__main__":
    uvicorn.run(os.getenv("APP_NAME"), host=os.getenv("HOST"), port=int(os.getenv("PORT")), reload=os.getenv("RELOAD") == "True")
