def LogTopN(LogFile,TopN=10):
	with open(LogFile,'r') as f:
		data_dict = {}
		data_list = []
		while True:
			data_info = f.readline()
			if not data_info:
				break
			else:
				data_item = data_info.split()
				temp = (data_item[0],data_item[6],data_item[8])
				data_list.append(temp)
		for k in data_list:
			#print k
			if k in data_dict:
				data_dict[k] += 1
			else:
				data_dict.setdefault(k,1)
		new_list = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)[:TopN]
		return new_list

#LogTopN(LogFile = 'access.txt')


if __name__ == '__main__':
	LogFile = 'access.txt'
	TopN = 5
	LogTopN(LogFile,TopN)
