#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#在介绍for循环之前，先介绍下range函数，这个函数可以在需要使用数字序列的时候，产生一个我们需要的数字序列，
#一定注意range的右边界不可达

#默认从0开始
print(list(range(5)))

#手动制定起始位置
print(list(range(0, 10)))

#指定间隔
print(list(range(0, 10, 2)))

#逆序
print(list(range(10, 0, -1)))

