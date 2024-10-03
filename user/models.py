from tortoise.models import Model
from tortoise import fields


class Students(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=10, description="姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    no = fields.CharField(max_length=10, description="学号")

    # 一对多
    Class = fields.ForeignKeyField("models.Class", related_name="students")

    # 多对多
    course_id = fields.ManyToManyField("models.Course", related_name="students")

    class Meta:
        table = "students"


class Class(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=10, description="班级名")


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=10, description="课程名")
    teacher = fields.ForeignKeyField("models.Teacher", related_name="teachers")


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=10, description="教师名")
    pwd = fields.CharField(max_length=32, description="密码")
    tno = fields.CharField(max_length=10, description="教师号")


