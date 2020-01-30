
class MFD(object):
    def __init__(self,user_name,user_passwd):
        self.user_name = user_name
        self.user_passwd = user_passwd

class UFD(object):
    def __init__(self,file_name,file_type,file_max_length,start,data='',is_memory=0,file_length=0):
        self.file_name = file_name
        self.file_type = file_type
        self.file_max_length = file_max_length
        self.file_length = file_length
        self.data = data
        self.start = start
        self.is_memory = is_memory     #是否在内存中，如果数据在内存中则不能对其进行删除

class disk_management(object):
    def __init__(self,start_disk=0,free_memory=0,per_size=64):
        # super().__init__()
        self.start = start_disk     #写入磁盘后随其更新
        self.free_memory = free_memory
        self.per_size = per_size
#内存管理，模块
class memory(object):
    def __init__(self,file_name,file_type,file_max_length,start,data,is_memory=0,file_length=0):
        self.file_name = file_name
        self.file_type = file_type
        self.file_max_length = file_max_length
        self.file_length = file_length
        self.data = data
        self.start = start
        self.is_memory = is_memory
    
class Block(object):
    def __init__(self,numpage=-1,accessed=0,time=0):
        self.numpage = numpage   #页号
        self.accessed = accessed  #访问次数
        self.time = time
class swap_me(object):
    def __init__(self,file_name=None,swap_data=None,block_file_length=4,swap_free_memory=124*64,):
        self.file_name = file_name
        self.swap_data = swap_data
        self.file_length = block_file_length  
        self.swap_free_memory = swap_free_memory
        # super().__init__()