#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数

def sign(x):
    if x > 0:
        print("正数")
    elif x == 0:
        print("zero")
    else:
        print("负数")
    return ""
print(sign(1))
print(sign(0))
print(sign(-1))
#函数默认都是有返回值的，如果不写，默认为None