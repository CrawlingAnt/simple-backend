from fastapi import APIRouter, Form
from typing import Union, Optional
from user.models import Students
from user.validator import StudentsValidator

router = APIRouter(prefix="/user", tags=['用户中心'])


@router.post("/")
async def all_students():
    students = await Students.all()
    for student in students:
        # 转换成字典
        print(vars(student))
    return {"students": students}


# 查询的条件非必填
@router.post("/query")
async def query_student(student: StudentsValidator):
    print('---', student)
    # student = await Students.filter(name=name)
    return {"message": 1}


# 返回除了密码外的数据
@router.post("/add")
async def add_student(student: StudentsValidator):
    print(student.model_dump())
    await Students.create(**student.model_dump())
    return {"message": "操作成功", "code": 200, "data": student.model_dump()}
