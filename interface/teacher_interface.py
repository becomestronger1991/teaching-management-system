from db import models


def check_course_interface(tea_name):
# 1.获取当前老师对象
    stu_obj=models.Teacher.select_data(tea_name)
    # 2.判断老师对象中的课程列表是否有值
    course_list=stu_obj.course_list
    # 3.若有则返回True，无则返回False
    if course_list:
        return course_list
    else:
        return False

def add_course_interface(course_name,teacher_name):
    teacher_obj=models.Teacher.select_data(teacher_name)
    course_list=teacher_obj.course_list
    if course_name in course_list:
        return False,f'教师【{teacher_name}】已经教授该课程'
    teacher_obj.add_course(course_name)
    return True,f'教师【{teacher_name}】已可以教授该课程'

def get_student_interface(course_name,teacher_name):
    # 1.获取当前老师对象
    tea_obj=models.Teacher.select_data(teacher_name)
    # 2.让当前老师对象，调用获取课程下所有学生
    student_list=tea_obj.get_student(course_name)
    # 3.判断课程下是否有学生
    if not student_list:
        return False,'课程下没有学生'
    return True,student_list

def change_score_interface(course_name,student_name,score,teacher_name):
    # 1.获取老师对象
    teacher_obj=models.Teacher.select_data(teacher_name)
    # 2.让老师对象调用修改分数方法
    teacher_obj.change_score(course_name,student_name,score)
    return True,f'学生【{student_name}】的课程【{course_name}】已修改为【{str(score)}】'