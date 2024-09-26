from fastapi import APIRouter, UploadFile
import os

router = APIRouter(
    prefix="/article",
    tags=["文章列表"],
)


@router.get("/")
async def hello():
    return {"message": "Hello World"}


@router.post('/upload')
async def upload(file: UploadFile):
    path = os.path.join('assets', file.filename)
    print(path)
    with open(path, 'wb') as f:
        for line in file.file:
            f.write(line)
    return {"filename": file.filename}