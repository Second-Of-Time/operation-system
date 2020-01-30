
import os,sys
import pandas as pd
import time
import threading

sys.path.append('./')
# from windows import next_window
os.chdir(os.path.dirname(sys.argv[0]))   #指定当前工作区
from threading import Thread
from main.classes import MFD,UFD,disk_management,memory,swap_me
from main.memory_management import initblock,FIFO,LRU

# from classes import MFD,UFD,disk_management,memory,swap_me
# from memory_management import FIFO,LRU


MAX_Disk = 900*64   #900块，每块大小为64B
Max_user = 10
Max_open = 5
Max_end = 0
user = []           #用户及目录
user_file = []      #用户文件
open_file = []      #打开文件
free_memory_out = [] #外存空闲区
ram_memory = []     #内存执行块
p=0                 #缺页数
swap_memory = []    #交换区
swap_free = []
swap_free.append(swap_me(None,None,0,64*124,))
user_name = 'first'

obstruct = []
dir = os.getcwd()+'\\main\\'
print(dir)
# C:\Users\lenovo\Desktop\操作系统课设\GUI\main\first_files.txt
def init_MFD():
    if os.path.exists('./main/MFD.txt'):
        file =  open('./main/MFD.txt','r') 
        string = file.readlines();
        
        if string:
            for i,lines in enumerate(string):
                user_name = lines.split(' ')[0]
                user_passwd = lines.split(' ')[1]
                user_passwd = user_passwd.split('\n')[0]
                user.append(MFD(user_name,user_passwd))
                # print(user[i].user_name,user[i].user_passwd,)
            return True
        else:
            create_MFD()
    return False

def init_disk():    
    '''
    初始化空闲分区
    '''
    free_memory_out.append(disk_management(start_disk=0,free_memory=900*64))

def show_free_disk():
    free_content = []
    free_blocks = 0
    for jk in range(len(free_memory_out)):
        free_blocks += free_memory_out[jk].free_memory
        # if jk == (len(free_memory_out )- 1):
        print('空闲盘区{} 开始盘块号{} 空闲区长度{} 空闲盘块数：{}'.format(jk,free_memory_out[jk].start,
        free_memory_out[jk].free_memory,free_blocks/free_memory_out[jk].per_size))
        free_content.append('空闲盘区{} 开始盘块号{} 空闲区长度{} 空闲盘块数：{}'.format(jk,free_memory_out[jk].start,
        free_memory_out[jk].free_memory,free_blocks/free_memory_out[jk].per_size))
    return free_content
    # print(f'空闲盘块数：{free_blocks/64}')

def create_MFD():
    same = False
    user_name = input('请输入创建的用户名称：')
    user_passwd = input('请输入用户密码：')
    while(1):
        for p in range(len(user)):
            if user_name == user[p].user_name:
                print('该用户已存在请重新出入：')
                same = True
        if same:
            user_name = input('请输入创建的用户名称：')
            user_passwd = input('请输入用户密码：')
        else:
            break;
    MFD.user_name = user_name
    MFD.user_passwd = user_passwd
    user.append(MFD)
    with open('./MFD.txt','a') as file:
        file.writelines(user_name+' '+user_passwd+'\n')
    file.close()


def Create_UFD(file_names):
    # file_name = input('请输入文件名：')
    flags = True
    file_name = file_names.split(' ')[0]
    print(f'file name:{file_name}')
    file_type = int(file_names.split(' ')[1])
    print(f'file type:{file_type}')
    file_max_length = int(file_names.split(' ')[2])
    print(f'file MAX length:{file_max_length}')
    while(1):
        flag = False
        for i in range(len(user_file)):
            if user_file[i].file_name == file_name:
                flag =  True
            else:flag =  False
        if flag:
            file_name = input('文件名已存在，请重新输入：')
        else:
            break;
    # file_type = int(input('请输入文件类型：//2表示可写   //1表示只读  //0表示不可操作：'))
    while 1:
        if file_type in [0,1,2]:
            break;
        else:
            file_type = int(input('输入有误，请重新输入：'))
    # file_max_length = int(input('请输入文件的最大容量：'))
    for j in range(len(free_memory_out)):
        if free_memory_out[j].free_memory < file_max_length:
            print(free_memory_out[j].free_memory)
            flags = False
            print('预分配磁盘空间失败！！！')
    if flags:
        for k in range(len(free_memory_out)):
            if file_max_length < free_memory_out[k].free_memory:
                if (file_max_length % 4) == 0:
                    blocks = file_max_length/4
                else:
                    blocks = int(file_max_length/4) + 1
                start =  free_memory_out[k].start   #disk_management.start_disk
                print('预分配盘块block',blocks)
                #对磁盘空闲区进行更新
                free_memory_out[k].start += blocks;
                free_memory_out[k].free_memory =free_memory_out[k].free_memory - blocks*64
                user_file.append(UFD(file_name,file_type,file_max_length,start))
                print('创建文件成功')
                return True

def Print_UFD():
    content = []
    if len(user_file)==0:
        print("抱歉,该用户没有创建任何文件,请先创建!!!")
    else:
        for i in range(len(user_file)):
            if user_file[i].file_type == 1:
                typrs = 'r-x'
            elif user_file[i].file_type == 2:
                typrs = 'rwx'
            else:
                typrs = '---'
            print('文件名：{} 最大文件长度{} 文件类型{} 起始位置{} 文件长度{}'.format(user_file[i].file_name,
            
            user_file[i].file_max_length,
            typrs,
            user_file[i].start,
            user_file[i].file_length
            ))
            content.append('文件名：{} 最大文件长度{} 文件类型{} 起始位置{} 文件长度{}'.format(user_file[i].file_name,
            user_file[i].file_max_length,
            typrs,
            user_file[i].start,
            user_file[i].file_length
            ))
            # next_window.textEdit.setPlainText
    return content

def system_menu():
    pass
def Delete_UFD(file_name):
    print(f'删除文件{file_name}')
    del_id = -1
    blocks = 0
    open_file_filename = []
    user_file_filename = []
    for j in range(len(open_file)):
        open_file_filename.append(open_file[j].file_name)
    for k in range(len(user_file)):
        user_file_filename.append(user_file[k].file_name)
    # file_name = input('请输入删除文件名：')
    if file_name in open_file_filename:
        print('抱歉,该文件已被打开,请先关闭,再进行删除操作!!!')
    elif file_name not in user_file_filename:
        print('该文件不存在！')
    else:
        for i in range(len(user_file)):
            if file_name == user_file[i].file_name:
                del_id = i
                if (user_file[i].file_max_length % 4) == 0:
                    blocks = user_file[i].file_max_length/4
                else:
                    blocks = int(user_file[i].file_max_length/4) + 1
        if user_file[del_id].is_memory:
            print('该文件已调入内存，删除失败！！！')
        else:
            free_memory_out.append(disk_management(user_file[del_id].start,blocks*64))
            del user_file[del_id]
            print('删除文件成功！！！')

def Open(file_name):
    open_file_filename = []
    user_file_filename = []
    for j in range(len(open_file)):
        open_file_filename.append(open_file[j].file_name)
    for k in range(len(user_file)):
        user_file_filename.append(user_file[k].file_name)
    if len(open_file_filename) > 5:
        print('打开文件超过上限值，请先关闭文件！！！')
        return False
    else:
        # file_name = input('请输入需要打开的文件名：')
        # print(open_file_filename,user_file_filename)
        if file_name in open_file:
            print('该文件已经打开！！！')
        elif file_name in (f for f in user_file_filename):
            for i in range(len(user_file)):
                if file_name == user_file[i].file_name:
                    open_file.append(user_file[i])
            print('该文件已经打开！！！')
            return True
        else:
            print('该文件不存在！！！')
            return False
        
    return False

def Write_File(file_names):
    file_name = file_names.split(' ')[0]
    file_length = int(file_names.split(' ')[1])
    data = file_names.split(' ')[2]

    open_file_filename = []
    
    for j in range(len(open_file)):
        open_file_filename.append(open_file[j].file_name)
    # file_name = input('请输入需要写的文件名：')
    if file_name in (fi for fi in open_file_filename):
        flag = False
        # file_length = int(input('请输入写入的长度：'))
        for i in range(len(user_file)):
            if file_name == user_file[i].file_name and file_length <= user_file[i].file_max_length:
                user_file[i].file_length = file_length
                # data = input('请输入指定长度的类容：')
                if len(data) <= file_length:
                    user_file[i].data = data
                    # free_memory_out.append(disk_management(file_length,(MAX_Disk - file_length)))
                    # user_file[i].start = 
                    flag = True
                    print('数据写入成功！！！')
                elif file_length > user_file[i].file_max_length or flag is False or len(data) > file_length:
                    print('欲写入的数据大小发生溢出,已超过文件的分配容量,写入失败!!!')
        
    else:
        print('文件没有打开，请先打开文件')
        

        

def Close(file_name):
    open_file_filename = []
    ram_memory_filename = []
    for j in range(len(open_file)):
        open_file_filename.append(open_file[j].file_name)
    for jk in range(len(ram_memory)):
        ram_memory_filename.append(ram_memory[jk].file_name)
    print(open_file_filename)
    # file_name = input('输入关闭的文件')
    if file_name in open_file_filename or file_name in ram_memory_filename:
        for i in range(len(open_file)):
            if file_name == open_file[i].file_name :
                del open_file[i]
        for k in range(len(ram_memory)):
            if file_name == ram_memory[k].file_name:
                del ram_memory[k]
                print('文件已关闭！')
        # print('关闭该文件后，打开的文件：',open_file_filename)
    # elif file_name in ram_memory_filename:
    #     for k in range(len(ram_memory)):
    #         if file_name == ram_memory[k].file_name:
    #             del ram_memory[k]
    #             print('文件已关闭！')
    else:
        print('关闭错误！文件尚未打开！')

def init_data(data,file_name):
    # memory_data = []
    for i in range(len(user_file)):
        if file_name == user_file[i].file_name:
            memory_data = user_file[i].data
    return memory_data

def Read_File(file_name):
    # file_name = input('请输入要查看的文件')
    if len(ram_memory) <= 4:
        print('内存空闲！！！允许调入内存')
        
        open_file_filename = []
        user_file_filename = []
        data = []
        for j in range(len(open_file)):
            open_file_filename.append(open_file[j].file_name)
        for k in range(len(user_file)):
            user_file_filename.append(user_file[k].file_name)
        if file_name in user_file_filename and file_name in open_file_filename:
            for file in range(len(user_file)):
                if file_name == user_file[file].file_name:
                    user_file[file].is_memory = 1       #调入内存执行
                    ram_memory.append(user_file[file])                                                                                   
                    if (user_file[file].file_length % 4) == 0:
                        block = user_file[file].file_length/4
                    else:
                        block = int(user_file[file].file_length/4 + 1)
                    # print(block)
                    if block is not None:
                        memory = init_data(user_file[file].data,file_name)
                        # print(type(memory))
                        # for p in range(block):
                        #     data.append(memory[p:p+4])
                        print(f'调入内存数据长度：{len(memory)}')
                        print(f'调入数据{memory}')
                        exchange_num = FIFO(memory,len(memory),p)
                        # print(exchange_num)
                        if exchange_num is not -1:
                            print('初次置换位置：',exchange_num)
                            swap_data = []
                            for num in range(len(memory)):
                                for nums in range(len(exchange_num)):
                                    if num == exchange_num[nums]:
                                        if len(memory[num:-1]) <=4:
                                            swap_data.append(memory[num:-1])
                                        else:
                                            swap_data.append(memory[num:num+4])
                            if swap_free[0].swap_free_memory > len(exchange_num)*4:
                                swap_free[0].swap_free_memory = 64*124-len(exchange_num)*4
                                swap_memory.append(swap_me(user_file[file].file_name,
                                swap_data,block_file_length = 4,swap_free_memory=64*124-len(exchange_num)*4,))
                            else:
                                print('交换区空间不足，无法交换！！！')
                            
        else:
            print('读入失败！！！不存在该文件，请重新读入')

    else:
        print('内存没有足够空间，调入内存失败！！！')
        threading_pool(file_name)


def show_file(file_name):
    Threads_concurrent(file_name)
    

def Threads_concurrent(file_name):
    if len(open_file) <= 4:
        threads = Thread(target=Read_File(file_name))  #开启并发线程
        threads.start()
        time.sleep(4)      #延迟

def threading_pool(file_name):
    if file_name not in obstruct:
        obstruct.append(file_name)
    choice = input('是否选择关闭文件y/n：')
    if choice == 'y':
        Close(file_name)
    else:
        for i in range(len(file_name)):
            Read_File(file_name)
            time.sleep(3)


def Save_UFD():
    # print(user_name)
    open(user_name+'_files'+'.txt','a')
    if len(user_file):
        for i in range(len(user_file)):
            with open(user_name+'_files'+'.txt','a')as file:
                file.writelines(user_file[i].file_name + ' '+
                str(user_file[i].file_max_length)+' '+
                str(user_file[i].file_type)+' '+
                str(user_file[i].start)+' '+
                str(user_file[i].file_length)+' '+
                user_file[i].data+'\n')
    file.close()

def Quit_System():
    print('保存主目录信息中...')
    Save_UFD()
    time.sleep(2)
    print('保存成功！')


def singn_in():
    user_name = input('请输入用户名：')
    user_passwd = input('请输入用户密码：')



def Scan_file():
    flags = True
    file = open(dir+user_name+'_files'+'.txt','r')
    strings = file.readlines()
    # print(strings)
    for i,lines in enumerate(strings):
        # print(type(lines))
        file_name = lines.split(' ')[0]
        file_type = int(lines.split(' ')[2])
        file_max_length = int(lines.split(' ')[1])
        start = int(lines.split(' ')[3])
        file_length = int(lines.split(' ')[4])
        data = lines.split(' ')[5]
        data = data.split('\n')[0]
        user_file.append(UFD(file_name,file_type,
        file_max_length,start,data,file_length=file_length))
        for j in range(len(free_memory_out)):
            if free_memory_out[j].free_memory < file_max_length:
                print(free_memory_out[j].free_memory)
                flags = False
                print('预分配磁盘空间失败！！！')
        if flags:
            for k in range(len(free_memory_out)):
                if file_max_length < free_memory_out[k].free_memory:
                    if (file_max_length % 4) == 0:
                        blocks = file_max_length/4
                    else:
                        blocks = int(file_max_length/4) + 1
                    start =  free_memory_out[k].start   #disk_management.start_disk
                    # print('预分配盘块block',blocks)
                    #对磁盘空闲区进行更新
                    free_memory_out[k].start += blocks;
                    free_memory_out[k].free_memory =free_memory_out[k].free_memory - blocks*64
    file.close()

def System_Init(user_name,user_passwd):
    init_disk();
    if (init_MFD()) is False :
        print('系统中不存在用户')
        create_MFD()
        # main_dir = input('系统中不存在用户，请输入主目录名：')
    else:
        # Print_Help();
        
        # user_name = input('登入用户，请输入登录的用户名称：')
        # user_passwd = input('请输入用户密码：')
        while 1:
            flag = False
            # for k in range(len(user)):
            #     print(user_name == user[k].user_name,'jk')
            #     print(user_passwd == user[k].user_passwd,'l;')
            for i in range(len(user)):
                if user_name == user[i].user_name and user_passwd == user[i].user_passwd:
                    Scan_file();
                    # Print_Help();
                    flag = True
                    break;
            if flag is False:
                print('输入有误，请重新输入')
                user_name = input('请输入创建的用户名称：')
                user_passwd = input('请输入用户密码：')
            else:
                break;
            

def Print_Help():
    print('************************操作系统实现*************************')
    print('*\t\t命令			  说明			*')
    # print("*\t\tlogin			登录系统		*") 
    print("*\t\tsignin			创建用户		*")
    print("*\t\tdelete			删除文件		*") 
    print("*\t\tcreate			创建文件		*") 
    print("*\t\topen			打开文件		*") 
    print("*\t\tclose			关闭文件		*")  
    print("*\t\tread			读取文件(调入内存显示)		*")  
    print("*\t\twrite			写入文件		*") 
    print("*\t\tls		        显示目录		*") 
    print("*\t\tshowdisk		空闲磁盘		*") 
    print("*\t\thelp			帮助菜单		*") 
    # print("*\t\tcls 			清除屏幕		*") 
    print("*\t\tlogout 			切换用户		*") 
    print("*\t\tquit			退出系统		*") 
    print("*****************************************************************") 

def file_system():
    while(1):
        # Print_Help()
        Command = input('请输入命令：')
        if Command=="create":
            Create_UFD()
        elif Command == 'delete':
            Delete_UFD();
        elif Command == 'signin':
            create_MFD();
        elif Command == 'open':
            Open()
        elif Command == "close":
            Close();
        elif(Command == "read"):
            show_file();
        elif(Command == "write"):
            Write_File();
        elif(Command == "quit"):
            Quit_System();
            break;
        elif(Command == "ls"):
            Print_UFD();
        elif(Command == "showdisk"):
            show_free_disk();

        elif(Command == "logout"):
            
            Quit_System();
            print("用户登出成功!!!")
            yes = input('是否继续使用(y/n)：')
            if yes == 'y':
                System_Init();
                file_system();
            else:
                os._exit(0)
        else:
            Print_Help();
            print('指令有误！请重新输入指令：')
	
def user_interface(user_name,user_passwd):
    System_Init(user_name,user_passwd)
    file_system()


if __name__ == '__main__':
    # init_MFD()
    System_Init();
    file_system();
