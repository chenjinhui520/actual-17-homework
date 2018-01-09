#!/usr/bin/env python
# -*- coding: UTF-8 -*
log_list = []
log_dict = {}
# get
log_file = open('./access.txt')
log = log_file.readlines()
log_file.close()
# format
for i in log:
    log_list.append((i.split()[0],i.split()[6],i.split()[8]))
# count
for j in log_list:
        log_dict[j] = log_dict.setdefault(j,0) + 1
# analysis
for count in range(10):
    k = log_dict.keys()[0]
    v = log_dict[k]

    for r in log_dict:
        if log_dict[r] > v:
            k = r
            v = log_dict[r]

    result = {k:v}
    log_dict.pop(k)
    print result.items()
