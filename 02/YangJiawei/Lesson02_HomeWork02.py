ls = []
i = 0
while i <= 10:
	print 'You have to input %d num for the function.' %(10-i)
	num = int(raw_input('Please input a num: '))
	if num not in ls:
		ls.append(num)
	i += 1
for j in range(len(ls)-1):
	for k in range(len(ls)-j-1):
		if ls[k] > ls[k+1]:
			ls[k],ls[k+1]=ls[k+1],ls[k]
print ls