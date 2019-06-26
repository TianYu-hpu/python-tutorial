#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#作用域
b = 2
def fun():
    '''
    函数内部定义的变量会隐藏外部同名变量，
    这里函数内外的b是两个完全独立的变量

    :return:
    '''

    def fun_inner():
        '''
        这里是一个内嵌函数，一般来说这种使用方式应该避免，但是在使用装饰器的时候，比较常用
        :return: 
        '''
        b = 3
        print(b)
        b = 4
        print(b)

    fun_inner()

fun()
print(b)