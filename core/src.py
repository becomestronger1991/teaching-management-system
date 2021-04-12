'''
用户视图层的主视图
'''
from core import admin,student,teacher


func_dic={
    '1':admin.admin_view,
    '2':teacher.stu_view,
    '3':student.stu_view
}


def run():
    while True:
        print('''
        ===========欢迎来到选课系统===========
                    1.管理员功能
                    2.教师功能
                    3.学员功能
        ================end================
        ''')
        choice=input('请输入功能编号：').strip()
        if choice=='q':
            break
        if not choice.isdigit() or choice not in func_dic:
            print('输入有误，请重新输入！')
            continue
        func_dic[choice]()