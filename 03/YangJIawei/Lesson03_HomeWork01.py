# -*- coding:utf-8 -*- 
#print 'Test:日志统计'
file = open('access.txt','r')
line_dict = {}
line_list = []
report_list = []
line = file.readline()
for line in file:
	if line == '\n':
		continue
	else:
		tmp_line = line.split(' ')
		IP, URL, STATUS = tmp_line[0], tmp_line[6], tmp_line[8]
		line_list.append((IP, URL, STATUS))
for k in line_list:
	if k in line_dict:
		line_dict[k] += 1
	else:
		line_dict.setdefault(k,1)
report_list = line_dict.items()
for j in range(len(report_list)):
	for i in range(len(report_list)-j-1):
		if report_list[i][1] < report_list[i+1][1]:
			report_list[i], report_list[i+1] = report_list[i+1], report_list[i]
print report_list[0:10]	 
file.close()