from fastapi import APIRouter, UploadFile, Request
import os

router = APIRouter(
    prefix="/article",
    tags=["文章列表"],
)


@router.post("/")
async def hello(headers: Request):
    print(dir(headers))
    return {"message": "Hello World"}


@router.post('/upload')
async def upload(file: UploadFile):
    path = os.path.join('assets', file.filename)
    print(os.getcwd())
    with open(path, 'wb') as f:
        for line in file.file:
            f.write(line)
    return {"filename": file.filename}
