#!/usr/bin/env python
#-*- coding:utf-8 -*-
_count = 0
num_list = []
flag = True
while flag:
    _count += 1
    number_input = int(raw_input('pls input number:'))
    if number_input not in num_list:
        num_list.append(number_input)
    if _count == 10:
        flag = False

print num_list
print len(num_list)

for i in range(len(num_list)-1):
    for j in range(len(num_list)-i-1):
        if num_list[j] > num_list[j+1]:
            num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
print num_list