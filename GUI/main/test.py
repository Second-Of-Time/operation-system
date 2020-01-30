import os,sys
os.chdir(os.path.dirname(sys.argv[0]))

class MFD(object):
    def __init__(self,user_name,user_passwd):
        self.user_name = user_name
        self.user_passwd = user_passwd
block = []


file =  open('C:\\Users\\lenovo\Desktop\\操作系统课设\\test_main\\MFD.txt','r')
string = file.readlines();
# print(string)
for i,line in enumerate(string):
    user_name = line.split(' ')[0]
    user_passwd = line.split(' ')[1]
    block.append(MFD(user_name,user_passwd))
    # print(block[i].user_name,block[i].user_passwd,)
    # print(i,line)
'''
for i in range(2):
    print(block[i].user_name,block[i].user_passwd,)
'''
li = [1,2,3]
f = 'third' in (j for j in (f for f in block))
# lambda x:1 in x.user_name
filter(lambda x:1 in x.user_name,block)
tuple(block).map(lambda x:x.user_name)
tuple


lis = ['as','sd']
lis.remove('as')

