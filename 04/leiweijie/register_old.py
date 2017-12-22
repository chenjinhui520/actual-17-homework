#!/usr/bin/env python
# encoding: utf-8
'''
@author: leiweijie
Create on2017年12月17日
'''
'''
基于文件存储的交互式用户登录注册系统
注册模块
实现功能：
    1.普通用户注册，并授权
    2.超级管理员注册（admin），并授权
使用方法：
    1.运行reister.py
'''
def userIsNotIn(user_name,user_file='users.txt'):
    '''判断用户名是否存在'''
    with open(user_file,'a+') as f:
        users_list = f.readlines()
        for user in users_list:
            if user.split(':')[0] == user_name:
                return user_name
def fileWrite(user_name,user_passwd,user_file='users.txt'):
    '''将用户名密码写入文件 ，并赋予权限，0最高权限，1普通用户，2锁定用户'''
    with open(user_file,'a+') as f:
        if user_name == 'admin':
            line = '%s:%s:0\n' %(user_name,user_passwd)
        else:
            line = '%s:%s:1\n' %(user_name,user_passwd)
        f.writelines(line)
def Register():
    '''用户注册'''
    user_name = raw_input('请输入用户名：').strip()
    if user_name:
        if not userIsNotIn(user_name):
            print '根据提示设置密码'
            user_passwd = raw_input('请输入密码：').strip()
            if user_passwd:
                confirm_passwd = raw_input('请再次输入密码：').strip()
                if user_passwd == confirm_passwd:
                    fileWrite(user_name,user_passwd)
                    print '注册成功'
                else:
                    print '密码不一致'
            else:
                print '密码不能为空'
        else:
            print '用户已存在'
    else:
        print '用户名不能为空'
if __name__ == '__main__':
    Register()       