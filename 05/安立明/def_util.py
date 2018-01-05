
#encoding=utf-8
import json
#从文件读取到列表
def file_to_dict():
    tmp_dict = {}
    with open('userlist.txt','r') as f:
        tmp_dict=json.loads(f.read())
    f.close()
    return tmp_dict

#从列表保存到文件
def dict_to_file(add_dict):
    tmp_dict = {}
    tmp_dict=file_to_dict()
    tmp_dict.append(add_dict)
    with open('userlist.txt','w') as f:
        f.write(json.dumps(tmp_dict))
    f.close()
    return 'ok'

#删除用户
def del_user(username):
    tmp_list=file_to_dict()
    for user in tmp_list:
        if user.get('name') == username:
            tmp_list.remove(user)
    with open('userlist.txt','w') as f:
        f.write(json.dumps(tmp_list))
    f.close()
    return True

#认证用户状态，通过返回True
def auth_user_status(username,password):
    tmp_list=file_to_dict()
    for user in tmp_list:
        print user.get('name'),user.get('passwd')
        if (user.get('name') ==username) and (user.get('passwd') ==password):
            return True
    else:
        return False

#判断用户是否存在
def find_user_exits(username):
     tmp_list=file_to_dict()
     for user in tmp_list:
         if user.get('name') ==username:
             return True
     else:
         return False

#获取用户信息
def get_user_info(username):
    tmp_list = file_to_dict()
    for user in tmp_list:
        if user.get('name') == username:
            return user







