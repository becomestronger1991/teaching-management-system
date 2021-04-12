import os

from db import models

def admin_regis(name,pwd):
    # 1.判断用户是否存在
    # 调用admin类中的select方法。由该方法去调用db——handler中的select data功能获取对象
    obj=models.Admin.select_data(name)
    if obj:
        return False,f'管理员{name}已存在'

    # 如果没有注册过，就调用类实例化管理员，然后把管理员对象存储在pickle文件中
    admin_obj=models.Admin(name,pwd)
    # 对象来调用save会把对象当作第一个参数自动传入
    admin_obj.save()
    return True,f'管理员{name}注册成功'



# 管理员创建学校信息
def create_school(schname,schaddr,admin_name):
    # 1. 先查看当前学校是否存在
    school_obj=models.School.select_data(schname)
    # 2. 若学校存在，则返回False告诉用户学校已经存在
    if school_obj:
        return False,f'学校[{schname}]已存在'
    # 3. 若不存在，则创建学校，注意：（由管理员对象来创建）
    admin_obj=models.Admin.select_data(admin_name)
    admin_obj.create_school(schname,schaddr)
    return True,f'学校[{schname}]创建成功'

def create_course(school,course_name,admin):
    # 1.查看课程是否存在
    school_obj=models.School.select_data(school)
    # 1.1 先获取学校对象中的课程列表
    if course_name in school_obj.course_list:
        return False,'当前课程已存在'
    # 1.2 判断当前课程是否存在在课程列表中
    admin_obj=models.Admin.select_data(admin)
    admin_obj.create_course(school,course_name)
    return True,f'课程{course_name}创建成功'

def create_teacher(teacher_name,admin_name,password='123'):
    # 1.先检查老师是否存在
    teacher_obj=models.Teacher.select_data(teacher_name)
    # 2.存在返回老师已经注册
    if teacher_obj:
        return False,f'老师{teacher_name}已存在'
    # 3.不存在则给老师注册，让管理员来创建
    admin_obj=models.Admin.select_data(admin_name)
    admin_obj.create_teacher(teacher_name,password)
    return True,f'老师{teacher_name}创建成功'
