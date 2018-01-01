# -*- coding:utf8 -*-

import pickle
import json

# 定义各种异常
def UsernameIsEmpty(username):
    '''检查用户输入是否为空，为空则触发异常'''
    # return True if username != '' else False
    if not username:
        raise Exception('{"username": "Username can not be empty"}')


def UsernameAlreadyExist(username, users):
    '''检查用户名是否已注册，如果已注册就触发异常'''
    if username in users:
        # format不是万能的，在下列情况下会失效，必须直接接在字符串外才行
        # 这种情况只能用%s
        # raise Exception('{"username": "[{}] already exist"}'.format(username))
        raise Exception('{"username": "The name already exists"}')


def CheckPassword(username, password, users):
    '''验证用户密码'''
    if users[username] != password:
        raise Exception("Username or password is invalid!")


def CheckLoginUser(username, users):
    '''检查要登陆的用户是否存在'''
    if username not in users:
        raise Exception("Username or password is invalid!")


def CheckPasswordLen(password):
    ''' 密码长度检测 '''
    if len(password) < 5:
        # raise Exception("The password length is at least 5 bits")
        raise Exception('{"password": "Length is at least 5"}')

def DoubleCheckPassword(password, repeat_password):
    '''密码二次验证'''
    if password != repeat_password:
        # raise Exception("Sorry, passwords do not match")
        raise Exception('{"retype_password": "Passwords do not match"}')

def CheckLoginIn(username, record):
    '''检查用户是否已登陆 '''
    if username in record:
        raise Exception("Username: [{}] has been logged in!".format(username))


def CheckChoice(choice, command):
    '''用户选项验证 '''
    if not choice.isdigit() or choice not in command:
        raise Exception("Usage: {}".format(command))

# 数据读取和写入接口
def userdata(filename, data=None):
    try:
        if data is None:
            with open(filename, 'rb') as point:
                return pickle.load(point)
        else:
            with open(filename, 'wb') as handle:
                pickle.dump(data, handle)
            return
    except IOError as err:
        users = {}
        return users
# 报错的args返回一个元组，如UsernameIsEmpty
# ('{"username": "Username can not be empty"}',)
# 取出第一个元素是一个json格式
# 有个疑问？自定义的其他异常，第一个元素有的是字符串，有的是json形式的字典
# 难道是，当Exception接受单一变量时，返回的都是json?
# 从测试结果来看是这样的
def get_key(data):
    dicterr = json.loads(data)
    return [key for key in dicterr.keys()][0]

# 当注册用户输入错误时，非错误框中还显示原来的提示信息
def get_dicterr(data):
    dicterr = json.loads(data)

    dicterr.setdefault('username', "Username")
    dicterr.setdefault('password', "Password")
    dicterr.setdefault('retype_password', "Retype password")

    return dicterr


# 返回那个用户被删除----未使用
def delete_user(duser):
    information = ''
    if duser == None:
        information = ''
    else:
        information = "{} has already deleted".format(duser)
    return information
