#!/usr/bin/env python
# -*- coding: UTF-8 -*-

num_str = raw_input('pls input ur num:')

for i in range(0,len(num_str)/2):
    if num_str[i] != num_str[-1-i]:
        print 'ur number is not palindrome'
        break
if i == len(num_str)/2 - 1:
    print 'ur number is palindrome'
