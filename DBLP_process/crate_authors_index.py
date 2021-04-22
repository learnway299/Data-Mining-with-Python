import codecs
from time import strftime, localtime
source = codecs.open('data/authors.txt','r','utf-8')
result = codecs.open('data/authors_encoded.txt','w','utf-8')
index = codecs.open('data/authors_index.txt','w','utf-8')
index_dic = {}
name_id = 0

# 打印当前时间
def printTime():
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    return

print("Authors' index create Start")
printTime()

for line in source:
    name_list = line.split(',')
    for name in name_list:
        if not (name == '\r\n'):
            if name in index_dic:
                index_dic[name][1] +=1
            else:
                index_dic[name] = [name_id,1]
                index.write(name + u'\r\n')
                name_id += 1
            result.write(str(index_dic[name][0]) + u',')
    result.write('\r\n')

source.close()
result.close()
index.close()
print(" Authors' index create End")
printTime()
#print sorted(index_dic.iteritems(), key = lambda a:a[1][1])