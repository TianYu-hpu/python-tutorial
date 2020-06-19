#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#格式化
str1 = "%s %s %d %.2f" % ("hello", "world", 123456,123.456)
print(str1)

#python风格字符串格式化
str2 = '{0} {1} {2} {3:.2f}'.format("hello", "world", 123456,123.456)
print(str2)

#python风格字符串格式化
str3 = '{} {} {} {:.2f}'.format("hello", "world", 123456,123.456)
print(str3)

x = 123.456
str4 = f'{"hello"} {"world"} {123456} {x:.2f}'
print(str4)

hello = "Hello, World"
for char in hello:
    print(char)

#字符串内建语法
str  = "hello"
print(str.capitalize())
print(str.upper())
#右边空格补齐
print(str.rjust(7))
#搜索替换
print(str.replace("hello", "world"))
#删除前后空白
print('Hello,  World!   '.strip())
print('Hello,  World!   '.replace(" ", ""))
