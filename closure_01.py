#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#闭包
#内层函数对外层函数非全局变量的引用
#例子:计算函数被调用了多少次

def fun_gen():
    count = 0
    def fun_closure(var):
        #生命，应用外部的变量
        nonlocal count
        print("got {}".format(var))
        count += 1
        print("invoked {} times".format(count))
    return fun_closure

fun = fun_gen()

fun(1)
fun("duck")

fun("i am iron man!")

