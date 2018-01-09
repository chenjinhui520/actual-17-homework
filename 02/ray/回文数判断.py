#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
Created on 2017-12-01
@author: leiweijie
'''
'''
需求：
判断用户输入的一串数字是不是回文数
回文数理解：
例如：12321、1221是回文数
思路：
知识点：

'''
# 方法1
# 思路：
#1.用户输入一串数字，求出数字一半的长度
#2.利用索引判断是否相等
while True:
    flag = 0
    user_input = raw_input('请输入一个数字：')
    user_input_len = len(user_input)
    for x in range(user_input_len/2):
        if user_input[x] == user_input[-x-1]:
            pass
        else:
            flag += 1
    if flag == 0 :
        print '是回文数'
    else:
        print '不是回文数'
