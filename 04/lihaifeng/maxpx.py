nlist = [(1,3),(4,7),(2,5),(2,1),(6,2),(4,1)]
print sorted(nlist,key=lambda i:max(i))
def max_num((x,y)):
	if x >= y:
		z = x
	else:
		z =y
	return z
print sorted(nlist,key=lambda i:max_num(i))	
