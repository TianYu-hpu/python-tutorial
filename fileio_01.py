#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#文件IO
#w是写入的意思，如果文件已经存在，会被清空
#a是append的意思，不会清空现在文件内容
#wb文件默认是文本文件打开，也可以用二进制模式打开
#rb 文本文件读取
f = open("/tmp/test.txt", mode="w")
f.write("12345\n")
f.write("67890\n")
f.writelines(["1", "2", "3", "4", "5"])
#打开的文件一定要关闭
f.close()

