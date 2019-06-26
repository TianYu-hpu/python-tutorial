#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数参数

def fun(var1, *var3, var2 = 3, **kw):
    '''
    这种情况，var2只能通过keyword传入，不然就被var3收集起来了
    :param var1:
    :param var2:
    :param var3:
    :param kw:
    :return:

    当结合使用的时候，定义函数需要遵循以下规则
    1.星号顺序参数必须在星号字典参数的前面
    2.顺序参数必须在keyword参数的前面
    3.keyword参数必须在星号字典的前面
    4.使用keyword参数来定义和使用函数
    '''
    print(kw)
    print(var3)
    print(var1, var2)

fun(1, 2, *[3, 4, 5], **{'var4': 4 , 'var5': 5, 'var6':6})
fun(1, 2, *[3, 4, 5], var2 = 100, **{'var4': 4 , 'var5': 5, 'var6':6})
#*号能语法也能用来传递字典类型的参数
