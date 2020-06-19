#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#decorator
#java中的注解
import  time

def trace(tag = "tag", flag = True):
    '''
    这个就是我们要用的带参数的decorator
    :param tag:
    :param flag:
    :return:
    '''

    print("got vars tag:[{}] flag:[{}]".format(tag, float))

    def decorator(fun):
        '''
        这个decorator其实是跟刚才上面定义的那个不带参数的trace最外层是一样的
        :param fun:
        :return:
        '''
        if flag:
            print("will trace:[{}]".format(fun))
        else:
            print("will not trace:{}".format(fun))

        def wrapper(*args, **kwargs):
            '''
            这个是decorator的返回值，一般是一个函数
            事实上，这个返回值的函数，会被用来代替decorate的函数被调用

            因此这个函数需要能处理任何参数输入
            :param args:
            :param kwargs:
            :return:
            '''
            print("inside trace the tag is :{}".format(tag))
            if flag:
                start = time.time()

            var = fun(*args, **kwargs)
            #在这个函数内部调用被decorate的函数
            #可以看出来，这里的fun是外面传递进来的，很典型的闭包
            if flag:
                period = time.time() - start
                print("used:[{}]".format(period))

            return var
        return  wrapper
    return decorator

def factorial(num):
    #阶乘函数 这里使用了递归的方式

    if num > 1:
        return num*factorial(num-1)
    else:
        return num
@trace(tag = "trace_2")
def compute(num = 128):
    factorial(num)

print("*" * 10)
compute(512)

