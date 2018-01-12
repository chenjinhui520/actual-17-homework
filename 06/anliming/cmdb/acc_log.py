import logdb
count_dict = {}
with open('access.txt') as f:
    for line in f:
        tmp = line.split()
        IP = tmp[0]
        URL = tmp[6]
        STATUS = tmp[8]
        count_dict[(IP,URL,STATUS)]=count_dict.get((IP,URL,STATUS),0)+1
    for ((ip,url,status),count) in count_dict.items():
        logdb.import_log(ip,url,status,count)