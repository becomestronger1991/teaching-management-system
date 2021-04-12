'''
管理员视图
'''
from interface import admin_interface,common_interface
from lib import common


LOGIN_NAME=None

# 管理员注册
def register():
    while True:
        username=input('请输入姓名：').strip()
        password=input('请输入密码：').strip()
        assure_pwd=input('请确认密码：').strip()
        if password==assure_pwd:
            # 调用逻辑接口层的管理员注册接口
            flag,msg=admin_interface.admin_regis(username,password)
            if flag:
                print(msg)
                return
            print(msg)
        else:
            print('两次密码输入不一致，请重新输入！')

# 管理员登陆
def login():
    while True:
        user=input('请输入姓名(按q退出)：').strip()
        if user.lower()=='q':break
        pwd=input('请输入密码：').strip()
        flag,msg=common_interface.login_interface(user,pwd,'admin')
        if flag:
            print(msg)
            # 记录登录状态
            global LOGIN_NAME
            LOGIN_NAME = user
            return
        print(msg)

# 管理员创建学校
@common.auth('admin')
def create_school():
    while True:
        school_name=input('请输入学校姓名：').strip()
        school_addr=input('请输入学校地址：').strip()
        # 学校名、学校地址、创建学校的管理员
        flag,msg=admin_interface.create_school(school_name,school_addr,LOGIN_NAME)
        if flag:
            print(msg)
            break
        print(msg)

@common.auth('admin')
def create_course():
    # 1.让管理员先选择学校
    while True:
        # 1.1 调用接口获取所有学校的名称并打印（封装在接口里面）
        flag,schoollist_or_msg=common_interface.get_all_school_name()
        if not flag:
            print(schoollist_or_msg)
            break
        for index,name in enumerate(schoollist_or_msg):
            print(f'编号：{index}  学校名称：{name}')
        choice=input('请输入学校编号：').strip()
        if not choice.isdigit():
            print('请输入正确编号！')
            continue
        choice=int(choice)
        if choice not in range(len(schoollist_or_msg)):
            print('请输入正确编号！')
            continue
        # 获取学校的名字
        school_name=schoollist_or_msg[choice]
        # 2. 选择学校后，再输入课程名称
        course_name=input('请输入课程名字：').strip()

        # 3. 调用创建课程接口，让管理员去创建课程
        flag,msg=admin_interface.create_course(
            school_name,course_name,LOGIN_NAME
        )
        if flag:
            print(msg)
            break
        print(msg)

@common.auth('admin')
def create_teacher():
    while True:
        # 1.让管理员输入创建老师的姓名
        teacher_name=input('请输入老师的姓名：').strip()
        flag,msg=admin_interface.create_teacher(teacher_name,LOGIN_NAME)
        if flag:
            print(msg)
            return
        print(msg)

func_dic={
    '1':register,
    '2':login,
    '3':create_school,
    '4':create_course,
    '5':create_teacher
}

def admin_view():
    while True:
        print('''
        1.注册
        2.登录
        3.创建学校
        4.创建课程
        5.创建讲师
        ''')
        choice = input('请输入功能编号：').strip()
        if choice=='q':
            break
        if not choice.isdigit() or choice not in func_dic:
            print('输入有误，请重新输入！')
            continue
        func_dic[choice]()

