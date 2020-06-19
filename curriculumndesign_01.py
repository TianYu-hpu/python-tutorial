#计算一个目录下的所有文件尺寸
import  os
path = "/home/tianyu/software"

def dir_size(d):
    '''
    递归版本
    '''

    dlist = os.listdir(d)
    #遍历所有内容
    allSize = 0
    for i in dlist:
        #为遍历的文件添加目录
        file = os.path.join(d, i)
        #判断是否是文件
        if os.path.isfile(file):
            m = os.path.getsize(file)
            allSize += m
        if os.path.isdir(file):
            #调用自己
            allSize += dir_size(file)
        return allSize

print("dir size:\t{}".format(dir_size(path)))