#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Exception handler
#默认的exception打印，获取的信息有限，调用一些内部的库，可以获得更多的信息
import traceback
import sys

try:
    raise  ValueError("this a a exp")
except Exception as ex:
    ex_type, ex_val, ex_stack = sys.exec_info()
    print(ex_type)
    print(ex_val)
    print(ex_stack)
    for stack in traceback.extract_tb(ex_stack)
        print(stack)






