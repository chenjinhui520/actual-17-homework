#!/usr/bin/python
dict1 = {}
dict2 = {}
tuple1 =()
list1 = []
list2 = []

for line in open("access1.txt"):
         tuple1 = (line.split(" ")[0],line.split(" ")[6],line.split(" ")[8])
	 if tuple1 not in dict1:
	        dict1[tuple1] = 1
	 else:
	        dict1[tuple1] += 1

list1 = dict1.values()
for i in range(10):
	for j in range(len(list1)-1):
		if list1[j] > list1[j+1]:
			list1[j],list1[j+1] = list1[j+1],list1[j]


list2 = list1[-1:-11:-1]
print list2

for k,v in dict1.items():
        	if v in list2:
	        	dict2[k] = v

print dict2
