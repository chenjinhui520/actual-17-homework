import logdb
def import_log(file,log_list_id):
    file = file
    count_dict = {}
    n=0
    with open(file) as f:
        for line in f:
            n=n+1
            tmp = line.split()
            IP = tmp[0]
            URL = tmp[6]
            STATUS = tmp[8]
            count_dict[(IP,URL,STATUS)]=count_dict.get((IP,URL,STATUS),0)+1
        for ((ip,url,status),count) in count_dict.items():
            logdb.im_log(ip,url,status,count,log_list_id)
    print n
    logdb.insert_log_count(log_list_id,n)
    f.close()