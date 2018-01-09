ls = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]
max1 = None
max2 = None
for num in ls:
	if num > max1 and num > max2:
		max1 = num
	if num < max1 and num > max2 :
		max2 = num
print 'The first is %s and the second is %s.' %(max1,max2)
		