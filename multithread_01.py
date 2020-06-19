#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#GIL(Global interpreter lock)

def count(num):
    var = 0
    for i in range(num + 1):
        var = var + i
    return var

#多线程执行，dummy是伪多线程，也就是多线程
#multiprecesing是多进程
from multiprocessing.dummy import Pool as ThreadPool
#创建一个线程池
p = ThreadPool()
results = p.map(count, range(10000))
#关闭线程池
p.close()
#等待线程池的所有任务完成
p.join()
#取得结果
print(results)




