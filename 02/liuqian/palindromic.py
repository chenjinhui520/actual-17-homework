#!/usr/bin/env python
number = int(raw_input("Enter input interger:"))
list1 = list(str(number)) 
count = 0
for i in range(0,len(list1)/2):
      if list1[i] != list1[-i - 1]:
         count += 1
print count
if count > 0:
   print 'Number is not palindromic number '
else:
   print 'Number is palindromic number' 

