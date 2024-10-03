from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
import user.urls as user_urls
import article.urls as article_urls
from tortoise.contrib.fastapi import register_tortoise
import settings.orm as settings_orm
import uvicorn
from middleware.blackList import BlackListMiddleware

app = FastAPI()
app.mount('/static', StaticFiles(directory='assets'), name='static')
register_tortoise(app=app, config=settings_orm.tortoise_orm)

# 添加中间件
app.add_middleware(BlackListMiddleware)

app.include_router(user_urls.router)
app.include_router(article_urls.router)

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
