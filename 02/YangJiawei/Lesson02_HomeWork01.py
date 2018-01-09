# -*- coding:utf-8 -*- 


num = raw_input('Please input a num: ')
ls1 = list(num)
ls2 = ls1[::-1]
if ls1 == ls2:
	print '这是一个回文数'
else:
	print '这不是个回文数'

