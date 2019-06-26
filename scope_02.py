#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#作用域
b = 2
def fun():
    b = 3
    '''
    函数内部定义的变量会隐藏外部同名变量，
    这里函数内外的b是两个完全独立的变量

    :return:
    '''

    def fun_inner():
        '''
        在内部函数中可以使用nonlocal来访问外部函数的变量，这种技术是在变成中称为闭包的一种技巧
        :return: 
        '''
        nonlocal b
        print(b)
        b = 4
        print(b)

    fun_inner()

fun()
print(b)