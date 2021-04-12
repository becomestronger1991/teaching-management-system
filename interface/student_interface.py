from db import models

def student_regis(username,password):
    # 1.判断用户是否存在
    # 调用admin类中的select方法。由该方法去调用db——handler中的select data功能获取对象
    obj = models.Student.select_data(username)
    if obj:
        return False, f'用户{username}已存在'

    # 如果没有注册过，就调用类实例化管理员，然后把管理员对象存储在pickle文件中
    admin_obj = models.Student(username, password)
    # 对象来调用save会把对象当作第一个参数自动传入
    admin_obj.save()
    return True, f'用户{username}注册成功'

def student_choose_school(school_name,stu_name):
    # 1.判断当前学生是否存在学校
    student_obj=models.Student.select_data(stu_name)
    if student_obj.school:
       return False,f'学生【{stu_name}】已经选择过学校了'
    # 若不存在则添加学校
    student_obj.choose_school(school_name)
    return True,f'学生【{stu_name}】已经成功选择学校【{school_name}】'

def get_course_list(stu_name):
    # 1.获取当前学生对象
    obj=models.Student.select_data(stu_name)
    school_name=obj.school
    # 2.判断当前学生是有学校，若灭有则返回False
    if not obj.school:return False,f'学生【{stu_name}】没有选择学校，请先选择学校'
    # 3.开始获取学校对象中的课程列表
    school_obj=models.School.select_data(school_name)
    # 3.1 判断当前学校中是否有课程，若没有，则联系管理员
    course_list=school_obj.course_list
    if not course_list:
        return False,f'学校【{school_name}】没有课程，请先联系管理员添加课程'
    # 3.2 若有，则返回课程列表
    return True,course_list

def choose_course(course_name,stu_name):
    # 1.先判断当前课程在不在学生对象的课表列表中
    obj=models.Student.select_data(stu_name)
    # 2.选择过则返回False
    if course_name in obj.course_list:
        return False,f'学生【{stu_name}】已经选择过当前课程'
    # 3.没选择过则返回True
    obj.choose_course(course_name)
    return True,f'学生【{stu_name}】成功选择课程【{course_name}】'

def check_grade(stu_name):
    stu_obj = models.Student.select_data(stu_name)
    if stu_obj.score:
        return stu_obj.score