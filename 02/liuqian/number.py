#!/usr/bin/env python
list1 = []
list2 = []
i = 0
while i < 10:
      number = int(raw_input('Enter integer Number:'))
      list1.append(number) 
      i += 1

for num in list1:
      if num not in list2:
         list2.append(num) 
      else:
         print 'num %s already in list2'%num


print list2

count = 0
#t = 0
#n = len(list2)-1
#for i in range(len(list2)-1):
#      for j in range(n):
#          if list2[j] > list2[j + 1]:
#             list2[j],list2[j + 1] = list2[j + 1],list2[j]
#             count += 1
#print t
changed = True
while changed:
    changed = False
    for i in range(len(list2) - 1):
        if list2[i] > list2[i+1]:
           list2[i], list2[i+1] = list2[i+1], list2[i]
           changed = True
           count += 1

print count
print list2
