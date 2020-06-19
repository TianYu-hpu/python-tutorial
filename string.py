#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#字符串
#python为了解决转义的问题，直接讲单双引号做等价，都可以用来定义字符串，一个字符串里面根据需要可以混用两种引号
#对于多行字符串可以用三单引号来定义

print('"hell"o, world')

hello = '''
    'Hello"",World!'
'''
print(hello)
print("lengh of hello", len(hello))

number = 1234
print("hello, how old are you!")
print(str(number));
print(int(str(number)), float(str(number)))

