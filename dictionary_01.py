#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#字典

dict = {"key":"value", "name":"tianyu", "age": 27}
#字典可以用下标获取
print(dict["key"])
#检查某个元素是否在字典里
print('key' in dict)
#设置某个元素的值，如果不存在则新加
dict["sex"] = "male"
print(dict["sex"])
#可以给一个默认值，避免keyError
print(dict.get("name", "N/A"))
#删除一个值
#比起删除，更喜欢直接用comprehension加判断条件直接创建一个新的值
del dict["sex"]
print(dict["打印不存在的元素会报错"])





