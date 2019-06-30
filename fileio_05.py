#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#文件IO
#w是写入的意思，如果文件已经存在，会被清空
with open("test.txt", mode="rb") as f:
    print(f.read())

