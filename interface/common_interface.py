import os
from conf import settings
from db import models

# 获取所有学校名称接口
def get_all_school_name():
    # 1.获取学校文件夹路径
    school_dir=os.path.join(settings.DB_PATH,'School')
    # 2.判断文件夹是否存在
    if not os.path.exists(school_dir):
        return False,'没有学校，请先联系管理员'
    # 3.文件夹若存在，则获取文件夹中所有文件的名字
    school_list=os.listdir(school_dir)
    list1=[]
    for i in school_list:
        name,format=i.split('.')
        list1.append(name)
    return True,list1

def login_interface(user,pwd,user_type):
    if user_type=='admin':
        obj=models.Admin.select_data(user)
    elif user_type=='student':
        obj=models.Student.select_data(user)
    elif user_type=='teacher':
        obj=models.Teacher.select_data(user)
    else:
        return False,'输入的用户角色不对，请输入正确角色'
    if obj:
        if pwd==obj.pwd:return True,f'用户【{user}】登陆成功！'
        else:return False,f'用户【{user}】密码输入错误'
    else:
        return False,f'用户【{user}】不存在'

def get_course_in_school(school_name):
    # 1.获取学校对象
    school_obj = models.School.select_data(school_name)
    # 2.获取学校对象下的所有课程
    course_list=school_obj.course_list
    if not course_list:
        return False,'该学校没有课程'
    return True,course_list