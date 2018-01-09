#!/usr/bin/env python
# encoding: utf-8
'''
@author: leiweijie
'''
'''
多用户登录
要求：
判断用户是否存在列表中，if else；（对列表循环遍历，取name值对比）
用户不存在，提示并退出；用户存在，提示输入密码，
判断密码是否正确，否：提示并退出；是：登录成功（登录后打印个人信息）
'''
users = [{'name':'wd','passwd':'wd','age':18,'job':'coo'},
         {'name':'panda','passwd':'panda','age':22,'job':'cto'},
         {'name':'ada','passwd':'ada','age':23,'job':'cio'}]

user_input = raw_input('请输入用户名：')
count = 0
for user_name in users:
    if user_input == user_name['name']:
        user_pwd = raw_input('请输入密码：')
        if user_pwd == user_name['passwd']:
            print '{0}登陆成功！ 姓名：{0} ，年龄：{1} ，工作：{2} '.format(user_name['name'],user_name['age'],user_name['job'])
            break
        else:
            print '密码错误，程序退出'
            break
    elif count < len(users)-1:
        count += 1
    else:
        print '用户不存在，程序退出'