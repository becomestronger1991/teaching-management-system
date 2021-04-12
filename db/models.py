"""
用于存放类
学校类，学员类，管理员类，教师类，课程类
"""
from db import db_handler

# 让所有子类来继承select和save方法
class Base:
    # 保存数据
    def save(self):
        db_handler.save_data(self)

    # 获取数据
    @classmethod
    def select_data(cls,username):
        obj=db_handler.select_data(cls,username)
        return obj

class Admin(Base):
    def __init__(self,user,pwd):
        self.name=user
        self.pwd=pwd

    def create_school(self,schname,schaddr):
        school_obj=School(schname,schaddr)
        school_obj.save()

    def create_course(self,school,course_name):
        # 1.调用课程类，实例化创建课程
        course_obj=Course(course_name)
        course_obj.save()
        # 2.获取当前学校对象，并将课程添加到课程列表中
        school_obj=School.select_data(school)
        school_obj.course_list.append(course_name)
        # 3.更新学校数据
        school_obj.save()

    def create_teacher(self,teacher_name,password):
        # 1.调用老师类，实例化得到老师对象，并保存
        teacher_obj=Teacher(teacher_name,password)
        teacher_obj.save()


class Student(Base):
    def __init__(self,username,password):
        self.name=username
        self.pwd=password
        # 每个学生只能有一个校区
        self.school=None
        # 一个学生可以选择多门课程
        self.course_list=[]
        # 学生的分数
        self.score={} # {'course_name':0}

    def choose_school(self,school_name):
        self.school=school_name
        self.save()

    def choose_course(self,course_name):
        # 1.学生课程列表添加课程
        self.course_list.append(course_name)
        self.score[course_name]=0
        self.save()
        # 2.学生选择的课程对象，添加学生
        course_obj=Course.select_data(course_name)
        course_obj.student_list.append(self.name)
        course_obj.save()

class Teacher(Base):
    def __init__(self,teacher_name,teacher_password):
        self.name=teacher_name
        self.pwd=teacher_password
        self.course_list=[]

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()

    def get_student(self,course_name):
        course_obj=Course.select_data(course_name)
        return course_obj.student_list

    def change_score(self,course_name,student_name,score):
        # 1.先获取学生对象
        student_obj=Student.select_data(student_name)
        # 2.再给学生能够对象中的课程修改分数
        student_obj.score[course_name]=score
        student_obj.save()

class Course(Base):
    def __init__(self,name):
        self.name=name
        self.student_list=[]

class School(Base):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        # 每所学校都应该有相应的课程，课程列表
        self.course_list=[]
