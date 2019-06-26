#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数参数

def fun(var1, var2, var3 = 3, var4 = 4, **kw):
    '''
    kw为可变参数，任何传入了，但是不属于前面定义的已知参数都会被手机到这个kw里面工处理，
    这个kw为python里面的字典类型
    :param var1:
    :param var2:
    :param var3:
    :param var4:
    :param kw:
    :return:
    '''
    print(kw)
    print(var1, var2, var3, var4)

fun(2, 1, var4 = 4, var5 = 5, var6 = 6)
