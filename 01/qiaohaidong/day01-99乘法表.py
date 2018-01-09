# -*- coding:utf8 -*-

for i in range(1, 10):
    for j in range(1, i+1):
        print "{0:2d} *{1:2d} = {2:2d}".format(i, j , i*j),
    print