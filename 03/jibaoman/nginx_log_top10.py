#!/usr/bin/env python
#-*- coding:utf-8 -*-
f = open('access.txt','r')
new_dict = {}
num_list = []
for line in f:
    if not line:
        break
    ip_url_status= line.split(' ')[0],line.split(' ')[6],line.split(' ')[8]
    if ip_url_status in new_dict:
        new_dict[ip_url_status] +=1
    else:
        new_dict[ip_url_status] = 1
new_list = new_dict.items()
for i in range(len(new_list)-1):
    for j in range(len(new_list)-i-1):
        if new_list[j][1] > new_list[j+1][1]:
            new_list[j],new_list[j+1] = new_list[j+1],new_list[j]
    if i >= 10 and new_list[-i][1] != new_list[-i-1][1]:
        for x in new_list[-i::]:
            num_list.append(x[1])
            num2_list = set(num_list)
        if len(num2_list) >= 10:
            break
print num2_list,len(num2_list)
for x in new_list[-i::]:
    print x
f.close()
