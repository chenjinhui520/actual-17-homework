#!/usr/bin/env python
# encoding: utf-8
'''
@author: leiweijie
Create on2017年12月17日
'''
'''
基于文件存储的交互式用户登录注册系统
登录模块
实现功能：
    1.普通用户登录
    2.admin用户登录
    3.用户锁定
使用方法：
    1.运行login.py
    2.admin用户具有解锁功能（如没有admin用户请在register.py里注册）
    3.如果admin用户锁定，请后台修改users.txt文件，将第一个字段admin存在的一行改为admin:admin:0，既重置用户名密码均为admin
'''
import sys
from register_old import userIsNotIn
def userLock(user_name):
    '''用户锁定'''
    with open('users.txt') as f:
        user_list = f.readlines()
        for user in user_list:
            if user.split(':')[0] == user_name:
                user_list[user_list.index(user)] = user.split(':')[0]+':'+user.split(':')[1]+':'+'2\n'
    with open('users.txt','w') as fs:
            fs.writelines(user_list)
def adminControl():
    '''管理员用于解锁用户'''
    print '''
                管理员指令
    1.解锁用户
    2.退出系统
    '''
    while True:
        user_control = raw_input('请输入指令：')
        if user_control == '1':
            user_unlock = raw_input('请输入需要解锁的用户')
            if userIsNotIn(user_unlock):
                with open('users.txt') as f:
                    user_list = f.readlines()
                    for user in user_list:
                        if user.split(':')[0] == user_unlock:
                            user_list[user_list.index(user)] = user.split(':')[0]+':'+user.split(':')[1]+':'+'1\n'
                with open('users.txt','w') as fs:
                        fs.writelines(user_list)
                print '%s解锁成功' % (user_unlock)
            else:
                print '用户不存在'
        elif user_control == '2':
            sys.exit()
        else:
            print '请输入正确指令'   
def isUserLocked(user_name):
    '''判断用户是否被锁定'''
    with open('users.txt','r') as f:
        user_list = f.readlines()
        for user in user_list:
            if user.split(':')[0] == user_name:
                if user.split(':')[2].strip() == '2':
                    #print '用户锁定，请联系管理员解锁'
                    return 2
    return 1
            
def Login():
    user_name = raw_input('请输入用户名：').strip()
    if user_name:
        if userIsNotIn(user_name):
            if isUserLocked(user_name) != 2:
                passwd_count = 0
                while passwd_count<3:
                    user_passwd = raw_input('请输入密码：')
                    with open('users.txt') as f:
                        user_list = f.readlines()
                        count = 1
                        for users in user_list:
                            if users.split(':')[0] == user_name and users.split(':')[1]==user_passwd:
                                print '登陆成功'
                                passwd_count =4
                                if user_name == 'admin':
                                    adminControl()
                            elif count<len(user_list):
                                count +=1
                            else:
                                print '密码错误'
                    passwd_count += 1
                    if passwd_count ==3:
                        userLock(user_name)
            else:
                print '用户被锁定，请联系管理员解锁'
        else:
            print '用户不存在'
    else:
        print '用户名不能为空'
if __name__ == '__main__':
#    while True:
        Login()