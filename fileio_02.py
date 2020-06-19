#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#文件IO
#w是写入的意思，如果文件已经存在，会被清空
f = open("/tmp/test.txt")
#一次把所有的东西打印出来
print(f.read())
#打开的文件一定要关闭
f.close()

