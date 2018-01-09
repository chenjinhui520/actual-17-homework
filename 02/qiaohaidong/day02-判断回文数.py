# -*- coding: utf-8 -*-
num = raw_input("Input digits: ")
reverse_num = num[::-1]

if reverse_num == num:
    print "{0} is a palindrome number".format(num)
else:
    print "{0} is not a palindrome number".format(num)
