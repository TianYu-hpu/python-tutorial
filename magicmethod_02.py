#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#魔术方法
#魔术方法是内建方法
import datetime
class my_len:
    def __len__(self):
        return int(datetime.datetime.now().timestamp())

print(len(my_len()))