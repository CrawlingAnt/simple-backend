from fastapi import APIRouter, Form
from typing import Union, Optional, List
from user.models import Students, Course
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
                                    name__contains=student.name).values("name", "no", "Class__name")
    print('---', student)
    return {"message": student}


@router.post("/add")
async def add_student(student: StudentsValidator):
    print(student.model_dump())
    try:
        # 名称不能重复
        current = await Students.filter(name=student.name).first()
        if current:
            raise Exception("用户名已存在")

        current_student = await Students.create(**student.model_dump(exclude={"course_id"}))
        # 学生和课程的多对多绑定，可以先清除可能已有的数据
        await current_student.course_id.clear()
        choose_course = await Course.filter(id__in=student.course_id)
        print('---', choose_course)
        await current_student.course_id.add(*choose_course)
        return {"message": "操作成功", "code": 200}
    except Exception as e:
        return {"message": "操作失败", "code": 400, "msg": str(e)}


@router.post("/update")
async def update_student(student_id: int):
    await Students.filter(id=student_id).update(name="test")
    return {"message": "更新成功", "code": 200}


@router.post("/delete")
async def delete_student(student_id: int):
    await Students.filter(id=student_id).delete()
    return {"message": "删除成功", "code": 200}
