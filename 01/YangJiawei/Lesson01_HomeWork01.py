for i in range(1,10):
	for j in range(1,10):
		print j,'*',i,'=','%2s' %(i*j),'\t',		
		if i==j:
			print '\n'
			break
			