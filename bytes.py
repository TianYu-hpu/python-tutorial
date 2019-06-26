#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#bytes
#bytes 的定义，在python3中是以b开头的
b = b'this is a bytes'
#bytes经过decode可以转化成string
print(b.decode())

str = "this is a bytes str"
#string也可以通过encode转化为bytes
print(str.encode())

print(str.encode(encoding="utf-8"))
print("你好，世界".encode(encoding="gb2312"))
print("你好，世界".encode(encoding="ascii"))


