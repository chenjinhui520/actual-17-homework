#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年12月6日

@author: leiweijie
'''
# 去重排序
# 用户输入数字后进行去重排序
# 思路:
# 1.初始化2个空列表
# 2.将用户输入的数字放入一个空列表
# 3.判断另一个用户输入的是否有重复，去重后放入另一个空列表
# 4.利用sort方法排序
while True:
    older_list = []
    new_list = []
    user_control = raw_input('输入p游戏开始，输入q游戏退出：')
    if user_control == 'p':
        for x in range(5):
            user_input = raw_input('请输入5个数字：')
            older_list.append(user_input)
            for y in older_list:
                if y not in new_list:
                    new_list.append(y)
        new_list.sort()
        print new_list
    elif user_control == 'q':
        break
    else:
        print '请输入正确指令'