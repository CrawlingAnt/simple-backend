from fastapi import FastAPI
import user.urls as user_urls
import article.urls as article_urls
import uvicorn

app = FastAPI()

app.include_router(user_urls.router)
app.include_router(article_urls.router)


if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
