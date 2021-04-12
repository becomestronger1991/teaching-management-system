'''
教师视图
'''
from lib import common
from interface import teacher_interface,common_interface
from db import models

LOGIN_NAME=None


def login():
    while True:
        username=input('请输入姓名(按q退出)：').strip()
        if username.lower()=='q':break
        password=input('请输入密码：').strip()
        flag,msg=common_interface.login_interface(username,password,'teacher')
        if flag:
            print(msg)
            global LOGIN_NAME
            LOGIN_NAME=username
            break
        print(msg)

@common.auth('teacher')
def check_course():
    course_list=teacher_interface.check_course_interface(LOGIN_NAME)
    if not course_list:
        print('该教师没有教授课程')
        return
    for index,value in enumerate(course_list):
        print(index,value)

@common.auth('teacher')
def choose_course():
    # 1.先打印所有学校，并选择
    while True:
        flag, school_list_or_msg = common_interface.get_all_school_name()
        if not flag:
            print(school_list_or_msg)
            break
        print()
        for index, school_name in enumerate(school_list_or_msg):
            print(index, school_name)
        print()
        choice = input('请输入上课学校的编号(按q退出)：').strip()
        if choice.lower() == 'q': break
        if not choice.isdigit():
            print('请输入编号！')
            continue
        choice = int(choice)
        if choice not in range(len(school_list_or_msg)):
            print('请输入正确编号')
            continue
        school_name = school_list_or_msg[choice]
        # 2.从选择的学校中获取所有的课程
        flag2,course_list=common_interface.get_course_in_school(school_name)

        if not flag2:
            print(course_list)
            break
        for index2, course_name in enumerate(course_list):
            print(index2, course_name)
        print()
        choice1 = input('请输入上课班级的编号(按q退出)：').strip()
        if choice1.lower() == 'q': break
        if not choice1.isdigit():
            print('请输入编号！')
            continue
        choice1 = int(choice1)
        if choice1 not in range(len(course_list)):
            print('请输入正确编号')
            continue
        course_name=course_list[choice1]
        # 3.调用选择教授课程接口，将该课程添加到老师的课程列表中
        flag3,msg3=teacher_interface.add_course_interface(course_name,LOGIN_NAME)
        if flag3:
            print(msg3)
            break
        else:
            print(msg3)




@common.auth('teacher')
def check_student():
    while True:
        # 1.调用获取当前老师下所有的课程并且打印
        course_list = teacher_interface.check_course_interface(LOGIN_NAME)
        if not course_list:
            print('该教师没有教授课程')
            break
        # 2.打印所有课程并让老师选择
        for index2, course_name in enumerate(course_list):
            print(index2, course_name)
        print()
        choice1 = input('请输入上课班级的编号(按q退出)：').strip()
        if choice1.lower() == 'q': break
        if not choice1.isdigit():
            print('请输入编号！')
            continue
        choice1 = int(choice1)
        if choice1 not in range(len(course_list)):
            print('请输入正确编号')
            continue
        # 3.获取当前课程名称
        course_name=course_list[choice1]
        # 4.利用当前课程名称获取所有学生
        flag,msg=teacher_interface.get_student_interface(course_name,LOGIN_NAME)
        if flag:
            print(msg)
            return
        print(msg)
        break

@common.auth('teacher')
def change_grade():
    # 1.先获取老师下所有的课程，并选择
    # 2.获取选择的课程下的学生，并选择修改的学生
    # 3.调用修改学生分数接口修改分数
    while True:
        # 1.调用获取当前老师下所有的课程并且打印
        course_list = teacher_interface.check_course_interface(LOGIN_NAME)
        if not course_list:
            print('该教师没有教授课程')
            break
        # 2.打印所有课程并让老师选择
        for index2, course_name in enumerate(course_list):
            print(index2, course_name)
        print()
        choice1 = input('请输入上课班级的编号(按q退出)：').strip()
        if choice1.lower() == 'q': break
        if not choice1.isdigit():
            print('请输入编号！')
            continue
        choice1 = int(choice1)
        if choice1 not in range(len(course_list)):
            print('请输入正确编号')
            continue
        # 3.获取当前课程名称
        course_name=course_list[choice1]
        # 4.利用当前课程名称获取所有学生
        flag,msg=teacher_interface.get_student_interface(course_name,LOGIN_NAME)
        if not flag:
            print(msg)
            return
        print()
        for index3,student_name in enumerate(msg):
            print(index3,student_name)
        print()
        choice3=input('请输入选择学生的编号：').strip()
        if not choice3.isdigit():
            print('请输入正确编号')
            continue
        choice3=int(choice3)
        if choice3 not in range(len(msg)):
            print('请输入正确编号')
            continue
        # 3.获得所选择课程的名称
        student_name=msg[choice3]
        score=input('请输入学生成绩：').strip()
        if not score.isdigit():
            print('请输入数字')
            continue
        # 调用接口修改成绩
        flag,msg=teacher_interface.change_score_interface(
            course_name,student_name,score,LOGIN_NAME
        )
        if flag:
            print(msg)
            return
        print(msg)
        break




func_dic={
    '1':login,
    '2':check_course,
    '3':choose_course,
    '4':check_student,
    '5':change_grade
}

def stu_view():
    while True:
        print('''
        1.登录
        2.查看教授课程
        3.选择教授课程
        4.查看课程下学生
        5.修改学生分数
        ''')
        choice = input('请输入功能编号：').strip()
        if choice=='q':
            break
        if not choice.isdigit() or choice not in func_dic:
            print('输入有误，请重新输入！')
            continue
        func_dic[choice]()