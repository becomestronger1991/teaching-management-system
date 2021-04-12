from conf import settings

import os,pickle

# 保存数据
def save_data(obj):
    '''
    1.获取对象的保存文件夹路径，以类名当作文件夹的名字
        obj.__class__：获取当前对象的类
        obj.__class__.__name__：获取类的名字
    '''
    class_name=obj.__class__.__name__
    PATH=os.path.join(settings.DB_PATH,class_name)
    # 2.判断文件夹是否存在，不存在则创建文件夹
    if not os.path.exists(PATH):
        os.mkdir(PATH)
    # 3.拼接当前文件的pickle路径，以用户名作为文件名
    user_path=os.path.join(PATH,f'{obj.name}.pkl')
    # 4.打开文件，保存对象
    with open(user_path,'wb') as f:
        pickle.dump(obj,f)

# 获取数据
def select_data(cls,username): # 类，username
    # 由cls类获取类名
    class_name=cls.__name__
    PATH=os.path.join(settings.DB_PATH,class_name)
    user_path = os.path.join(PATH, f'{username}.pkl')

    if os.path.exists(user_path):
        with open(user_path,'rb') as f:
            obj=pickle.load(f)
            return obj
    else:
        return None