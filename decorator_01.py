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

def compute(num = 128):
    factorial(num)

start = time.time()
factorial(100)
end = time.time()
period = end - start
print("used:[{}]ms".format(period))