#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数

def hello(name, upper = False):
    if upper:
        print("hello, %s" % name.upper())
    else:
        print("hello, %s" % name)

#在不写keyword的情况下，也可以按照顺序判断传入额是哪个参数
#python里面的参数，只要制定了name,就可以识别，不需要按照定义的顺序给出
hello("Michael", upper=True)
hello(upper=True, name = "Michael")
hello("Michael", True)
hello("rain")