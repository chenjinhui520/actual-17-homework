#!/usr/bin/env python
# encoding: utf-8
'''
@author: leiweijie
Create on2017年12月22日
'''
'''
根据列表里每个元组中最大值进行排序（简单）
[(1, 3), (4, 7), (2, 5), (2, 1), (6, 2), (4, 1)]
期待结果：[(2, 1), (1, 3), (4, 1), (2, 5), (6, 2), (4, 7)]
要求：用sorted和lambda完成
级别1：用lambda中用max
级别2：lambda中不用max    （思路：自己写一个max函数）
'''
#方法1
my_list = [(1, 3), (4, 7), (2, 5), (2, 1), (6, 2), (4, 1)]
print sorted(my_list,key=lambda (x,y):max(x,y))

#方法2
def my_max(a,b):
    if a > b:
        return a
    else:
        return b
my_list = [(1, 3), (4, 7), (2, 5), (2, 1), (6, 2), (4, 1)]
print sorted(my_list,key=lambda (x,y):my_max(x,y))
