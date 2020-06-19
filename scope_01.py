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
        使用golbal可以让函数内部能够访问外部变量定义而不会引起覆盖
        :return: 
        '''
        global b
        b = 3
        print(b)
        b = 4
        print(b)

    fun_inner()

fun()
print(b)