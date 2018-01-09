#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# input
count = 0
input_list = []

print 'pls input 10 nums!!!\n'

while count < 10:
    input_str = raw_input('pls input ur num:')
    if True == input_str.isdigit():
        input_list.append(input_str)
        count += 1
    else:
        print 'ur input is not correct,pls input again:'

print input_list

# distinct
dis_input = []
for i in input_list:
    if i not in dis_input:
        dis_input.append(i)

print dis_input

# sort
for i in range(len(dis_input)-1):
    for j in range(len(dis_input)-i-1):
        if int(dis_input[j]) > int(dis_input[j+1]):
            # 这个比较是个坑，输入进来的是字符串，比的时候有问题,艹
            dis_input[j],dis_input[j+1] = dis_input[j+1],dis_input[j]
print dis_input
