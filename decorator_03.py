#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#decorator
#java中的注解
import time

def factorial(num):
    #阶乘函数 这里使用了递归的方式

    if num > 1:
        return num*factorial(num-1)
    else:
        return num

def trace(fun):
    #这个就是我们要用的decorator

    print("will trace:{}".format(fun))

    def wraper(*args, **kwargs):
        '''
        这个是decorator的返回值，一般是一个返回值
        事实上，这个返回值的函数，会被用来替代被decorate的函数调用

        因此这个函数需要能处理任何参数输入，因为很多时候，一个decorator并不知道要被
        decorate的函数是什么样子，接受什么样的参数，因此我们使用*来解决这个问题
        :param args:
        :param kwargs:
        :return:
        '''

        start = time.time()

        var = fun(*args, **kwargs)

        #在这个函数内部调用被decorate的函数
        #可以看出来这个fun是最外面传进来的，很典型的闭包

        period = time.time() - start
        print("used:{}".format(period))

        #处理fun的返回值
        return var
    return wraper

@trace
def compute(num):
    '''
    这里我们要定义的是compute,实际定义的也是compute
    但是经过trace里面的decorate,在运行空间里面的compute就被替换成
    trace里面的wrapper,所以最终compute调用的时候是trace里面的wrapper
    :param num:
    :return:
    '''
    factorial(num)

start = time.time()
factorial(100)
end = time.time()
period = end - start
print("used:[{}]ms".format(period))

compute_wrapped = trace(compute)

#这里compute_warpped其实就是trace里面的wrapper
print("*" * 100)
ret = compute_wrapped(512)
#调用compute_wrapped就是调用wrapper,wrapper内部再调用compute
