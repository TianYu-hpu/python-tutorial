#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#tuples
#元组是不可变的list,其使用跟list一致，不同的是list的元素可变，而tuple不可变，同时tuple可以作为dict的key,而list不行
dict = {(x, x + 1): x for x in list(range(10))}

print(dict)

tuples = (5, 6)
print(type(tuples))

print(tuples[1])

print(dict[tuples])

print(dict[1,2])

#多元赋值
def fun():
    return 1, 2, 3, 4
var = fun()
print(var)
print(type(var))

var1, var2, var3, var4 = fun()
print(var1)
print(var2)
print(var3)
print(var4)

def swap(vara, varb):
    vara, varb = varb, vara
    return vara, varb
print(swap(1, 2))
