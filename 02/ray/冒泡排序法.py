#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年12月5日

@author: leiweijie
'''
# 冒泡排序法
# 思路：
# 冒泡排序法：
# 1.相邻两个数进行大小比较，前一个数大于后一个数就进行位置互换
# 2.首次的互换次数为长度减1
# 3.每一次互换后内层互换次数减1
test_list = range(10,0,-1)
for x in range(0,len(test_list)-1):
    for y in range(0,len(test_list)-x-1):
        if test_list[y] > test_list[y+1]:
            test_list[y],test_list[y+1] = test_list[y+1],test_list[y]
print test_list