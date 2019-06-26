#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#字典
import json

dict = {"key":"value", "name":"tianyu", "age": 27}

for key in dict:
    value = dict[key]
    print("key {} value {}".format(key, value))

for key, value in dict.items():
    print("key %s value: %s" % (key, value))

#comprehension
nums = [0,1,2,3,4,5]
even_num_to_squre = {x: x ** 2 for x in nums if(x % 2 == 0)}
print(even_num_to_squre)

var_json = json.dumps(dict)
print(type(var_json))
print(var_json)

dict2 = json.loads(var_json)
print(type(dict2))
print(dict2)



