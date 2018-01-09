#!/usr/bin/env python
#-*- coding:utf-8 -*-

number_input = raw_input('pls input number:')

num_list = []
#
# print len(number_input)
for i in number_input:
    num_list.append(i)
if num_list == num_list[::-1]:
    print "%s是回文数"%number_input
else:
    print '%s不是回文数'%number_input
