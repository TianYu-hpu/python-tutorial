#计算一个目录下的所有文件尺寸
import  os
path = "/home/tianyu/software"

def dir_size(d):
    '''
    递归 comprehension版本
    '''

    dlist = [os.path.join(d, i) for i in os.listdir(d)]
    #遍历所有内容
    allSize = sum([os.path.getsize(file) for file in dlist if os.path.isfile(file)])

    allSize += sum([dir_size(file) for file in dlist if os.path.isdir(file)])

    return allSize

print("dir size:\t{}".format(dir_size(path)))