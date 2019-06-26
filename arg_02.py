#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数参数

def fun(var1, var2, *var3):
    '''
    对于不带keyword的顺序参数，可以使用星号语法进行收集
    :param var1:
    :param var2:
    :param var3:
    :return:
    '''
    print(var3)
    print(var1, var2)

fun(1, 2, 3, 4, 5)
#*号能收集参数，也能用来传递参数
fun(1, 2, *[3, 4, 5])
