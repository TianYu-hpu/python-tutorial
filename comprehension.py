#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list
#list中的数组可以灵活的增删，而且可以存储不同类型的数据
list = [1, 2, 3, 4]
print(list, list[2])
print(list[-1])
print(len(list))
list[2] = 'Hello, World!'
print(list)
list.append("你好")
print(list)
list.pop()
print(list)

#slicing/切片
#获得地2个元素到第4个元素，左边界可达，右边界不可达
print(list[1:3])
#逆序获得元素
print(list[1:3:-1])
#step
print(list[0:-1:2])
#索引号可以省略，代表获取到最后
print(list[0:])
list[2:3] = [3]
print(list)