#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数参数

def fun(var1, var2, *var3, **kw):
    '''
    顺序参数、keywork参数和变成参数可以结合起来使用
    :param var1:
    :param var2:
    :param var3:
    :param kw:
    :return:
    '''
    print(kw)
    print(var3)
    print(var1, var2)

fun(1, 2, *[3, 4, 5], **{'var4': 4 , 'var5': 5, 'var6':6})
#*号能语法也能用来传递字典类型的参数
