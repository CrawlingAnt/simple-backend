from fastapi import APIRouter, Form
from typing import Union, Optional, List
from user.models import Students
from user.validator import StudentsValidator
from user.validator import StudentsQueryValidator

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
async def query_student(student: StudentsQueryValidator):
    print('---', student.model_dump(exclude_none=True, exclude={'name'}))
    # 去除空值和名称的模糊搜索
    student = await Students.filter(**student.model_dump(exclude_none=True, exclude={'name'}),
                                    name__contains=student.name).values("name", "no")
    print('---', student)
    return {"message": student}


@router.post("/add")
async def add_student(student: StudentsValidator):
    print(student.model_dump())
    # 名称不能重复
    current = await Students.filter(name=student.name).first()
    if current:
        return {"message": "名称不能重复", "code": 400}
    else:
        await Students.create(**student.model_dump())
        return {"message": "操作成功", "code": 200, "data": student.model_dump()}
