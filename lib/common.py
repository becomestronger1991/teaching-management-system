


# 多用户登录认证装饰器
def auth(role):
    def login(func):
        def wrapper(*args,**kwargs):
            # 如果把模块导入放在外面会出现循环导入
            from core import admin, student, teacher
            if role =='admin':
                if admin.LOGIN_NAME:
                    res=func(*args,**kwargs)
                    return res
                admin.login()

            elif role=='teacher':
                if teacher.LOGIN_NAME:
                    res=func(*args,**kwargs)
                    return res
                teacher.login()

            elif role=='student':
                if student.LOGIN_NAME:
                    res=func(*args,**kwargs)
                    return res
                student.login()

            else:
                print('当前视图没有权限')

        return wrapper
    return login
