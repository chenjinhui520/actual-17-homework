#!/usr/bin/env python
#coding:utf8

nginx_list = {}
sort_list = []

f = open('access.txt', 'r')
for line in f.readlines():
	nginx_list[(line.split(" ")[0],line.split(" ")[6],line.split(" ")[8])] = nginx_list.setdefault((line.split(" ")[0],line.split(" ")[6],line.split(" ")[8]),0) +1
f.close()

for k,v in nginx_list.items():
	sort_list.append((k,v))

for i in range(0,10):
	for j in range(i+1,len(sort_list)):
		if sort_list[i][1] < sort_list[j][1]:
			sort_list[i],sort_list[j] = sort_list[j],sort_list[i]
	print sort_list[i]
