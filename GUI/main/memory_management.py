
import random
import time
from main.classes import Block
# from classes import Block

block_size = 4  #内存块大小
size=4          #分配该进程的内存块数目
count=0         #记录指令的序号
p=0             #缺页数目
block=[]        #内存块

data = []


def printzhiling(ls):
    for i in range(size):
        print(block[i].numpage,'--',block[i].accessed)

def findpage(block,curpage):  #查找指令是否被调如内存
    for i in range(size):
        if block[i].numpage == curpage:
            return i
    return -1
def findexchange(block):    #查找最先进入内存的指令
    first = 0
    for i in range(size):
        if block[i].accessed > block[first].accessed:
            first = i
    return first
def findspace(block):   #查找空闲内存
    for i in range(size):
        if block[i].numpage == -1:
            return i
    return -1
def findexchange_time(block):
    time = block[0].time
    change = 0
    for i in range(size):
        if block[i].time < block[change].time:
            time = block[i].time            
            change = i
    return change


def initblock():
    for i in range(size):
        
        # if i<4:
        #     block.append(Block(numpage=n,accessed=1))
        # block = []
        block.append(Block(numpage=-1,accessed=0,time=0))
def FIFO(data,n,p):
    initblock()         #初始化页面
    exchange_nums = []
    z = 1
    for i in range(n):
        # print(data[i])
        curpage = int(i/block_size)#计算当前页数
        # print('curpage:',curpage)

        # print(findpage(block,curpage),'---',i)
        if findpage(block,curpage) != -1:
            pass
            # print(f'{data[i]}  指令已调入  页号：{findpage(block,curpage)}')
        elif findpage(block,curpage) == -1:
            p += 1
            if findspace(block) == -1:    #没有找到空闲内存块
                
                exchange_num = findexchange(block)   #找到置换出的页号
                block[exchange_num].numpage = curpage
                block[exchange_num].accessed = -1  #置换出的指令页数初始化
                infos = []
                for l in range(0,len(data),4):
                    infos.append(data[l:l+4])
                print(f'第{z}次置换')
                if z == 1:
                    print(data[0:16])
                else:
                    print(data[z*4:z*4*4])
                z += 1
                # print(i)
                exchange_nums.append(i)
                time.sleep(5)
            else:
                block[findspace(block)].numpage = curpage
                
        for j in range(size):
            block[j].accessed += 1
    if len(data)/4 <= 4:
        show_info(data)
    # print(p,'   ',n)
    # print(f'缺页次数：{p} \t 缺页率是：{p/n*100}%')
    # 返回置换出的页号
    if len(exchange_nums)  != 0:
        # print(exchange_nums)
        return exchange_nums
    else:
        return -1
    
def show_info(data):
    info = []
    for i in range(0,len(data),3):
        info.append(data[i:i+3])
    if len(data)/4 >= 4:
        for i in range(len(info)):
            print('第{}块内存块数据：{}'.format(i,info[i]))
            time.sleep(4)
    # elif exchange_nums:
    #     print(f'进行了{len(exchange_nums)}次内存调度')
    #     for k in range(len(exchange_nums)):
    #         for j in range(4):
    #             print('第{}块内存块数据：{}'.format(i,info(i)))

def OPT(data,n,p):
    initblock(block)
    exchange_num = -1
    for i in range(n):
        curpage = int(data[i]/block_size)
        # print('curpage:',curpage)
        if findpage(block,curpage) != -1:
            pass
            # print(f'{data[i]}  指令已调入   页号：{findpage(block,curpage)}')
        elif findpage(block,curpage) == -1:
            if findspace(block) == -1: 
                for f in  range(size):
                    for g in range(i,n):
                        if block[f].numpage != int(data[g]/block_size):  #不存在则将时间调为无穷
                            block[f].accessed = random.randint(1000,10000)
                        else:
                            block[f].accessed = g
                            break;
                exchange_num = findexchange(block)
                block[exchange_num].numpage = curpage
                exchange_num = i
                p += 1
                # block[exchange_num].accessed = -1  #置换出的指令页数初始化
            else:
                block[findspace(block)].numpage = curpage
                p += 1
        for j in range(size):
            block[j].accessed += 1
    print(f'缺页次数：{p} \t 缺页率是：{p/n*100}%')
    # 返回置换出的页号
    if exchange_num is not -1:
        print(exchange_num)
        return exchange_num
    else:
        return -1
    
def LRU(data,n,p):#最近最久未使用
    initblock(block)
    exchange_num = []
    for i in range(n):
        curpage = int(data[i]/block_size)
        
        if findpage(block,curpage) != -1:
            pass
            # print(f'{data[i]}  指令已调入  页号：{findpage(block,curpage)}')
        elif findpage(block,curpage) == -1:  #没有找到空闲内存，执行LRU算法 load... ...
            if findspace(block) == -1:
                
                block[findexchange_time(block)].numpage = curpage
                p += 1
                block[findexchange_time(block)].time = time.time()
                block[findexchange_time(block)].accessed = -1
                exchange_num.append(i) 
            else:
                block[findspace(block)].numpage = curpage
                block[findspace(block)].time = time.time()
                p += 1
        for j in range(size):
            block[j].accessed += 1
    print('缺页次数：{} \t 缺页率是：{:.6f}%'.format(p,p/320*100))
    # 返回置换出的页号
    if len(exchange_num) != 0 :
        
        return exchange_num
    else:
        return -1



def initdata(zhiling,n):
    flag = 0
    print("请输入第一条指令：")
    # first = int(input())
    first = random.randint(1,n)
    print(f'第一条指令为{first}')
    for i in range(320):
        zhiling.append(first)
        if flag % 2 ==0:
            first += 1
            first = first%320
        if flag == 1:
            first = random.randint(0,first)
        if flag == 3:
            first=first+1+random.randint(0,320-first-1)
        flag += 1
        flag = flag % 4
    # print('长度：',len(zhiling),'\t','指令序列：',zhiling)
    
    data = zhiling
    print(data)
    return data
   
if __name__ == '__main__':
    n=320
    data = initdata(data,n)
    initblock()
    # printzhiling(block)
    print('OPT算法：')
    # OPT(data,n,p)
    print('LRU算法：')
    # LRU(data,n,p)
    print('FIFO 算法：')
    FIFO(data,n,p)
    