'''
学生视图
'''
from lib import common
from interface import student_interface,common_interface

LOGIN_NAME=None

def register():
    while True:
        username = input('请输入姓名：').strip()
        password = input('请输入密码：').strip()
        assure_pwd = input('请确认密码：').strip()
        if password == assure_pwd:
            # 调用逻辑接口层的管理员注册接口
            flag, msg = student_interface.student_regis(username, password)
            if flag:
                print(msg)
                return
            print(msg)
        else:
            print('两次密码输入不一致，请重新输入！')

def login():
    while True:
        username=input('请输入姓名(按q退出)：').strip()
        if username.lower()=='q':break
        password=input('请输入密码：').strip()
        flag,msg=common_interface.login_interface(username,password,'student')
        if flag:
            print(msg)
            global LOGIN_NAME
            LOGIN_NAME=username
            break
        print(msg)

@common.auth('student')
def choose_school():
    while True:
        # 先打印所有学校，让学生选择
        flag,school_list_or_msg = common_interface.get_all_school_name()
        if flag:
            print()
            for index,school_name in enumerate(school_list_or_msg):
                print(index,school_name)
            print()
            choice=input('请输入上课学校的编号(按q退出)：').strip()
            if choice.lower()=='q':break
            if not choice.isdigit():
                print('请输入编号！')
                continue
            choice=int(choice)
            if choice not in range(len(school_list_or_msg)):
                print('请输入正确编号')
                continue
            school_name=school_list_or_msg[choice]
            flag,msg=student_interface.student_choose_school(school_name,LOGIN_NAME)
            if flag:
                print(msg)
                break
            print(msg)
        else:
            print(school_list_or_msg)


@common.auth('student')
def choose_course():
    while True:
        # 1.获取当前学生所在学校的课程列表
        flag,msg_or_course_lis=student_interface.get_course_list(LOGIN_NAME)
        # 2.打印课程列表，并让用户选择课程
        if not flag:
            print(msg_or_course_lis)
            break
        print()
        for index,value in enumerate(msg_or_course_lis):
            print(index,value)
        print()
        choice=input('请输入选择课程的编号：').strip()
        if not choice.isdigit():
            print('请输入正确编号')
            continue
        choice=int(choice)
        if choice not in range(len(msg_or_course_lis)):
            print('请输入正确编号！')
            continue
        # 3.获取选择的课程的名称
        course_name=msg_or_course_lis[choice]
        # 4.调用学生选择课程接口
        flag,msg=student_interface.choose_course(course_name,LOGIN_NAME)
        if flag:
            print(msg)
            break
        print(msg)


@common.auth('student')
def check_grade():
    score=student_interface.check_grade(LOGIN_NAME)
    if not score:
        print('该学生没有选择课程')
        return
    for k,v in score.items():
        print(k,v)

@common.auth('student')
def pay_tuition():
    ...

func_dic={
    '1':register,
    '2':login,
    '3':choose_school,
    '4':choose_course,
    '5':check_grade,
    '6':pay_tuition
}

def stu_view():
    while True:
        print('''
        1.注册
        2.登录
        3.选择校区
        4.选择课程
        5.查看分数
        6.交学费
        ''')
        choice = input('请输入功能编号：').strip()
        if choice=='q':
            break
        if not choice.isdigit() or choice not in func_dic:
            print('输入有误，请重新输入！')
            continue
        func_dic[choice]()
