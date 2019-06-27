#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#generator
def my_list():
    for i in [1,2,3,4,5]
        #generator看上去就像是一个普通的函数，只不过把return替换成yield
        yield i
#每次执行到yield的时候，函数都会返回一个值，但是并不结束
#而是把中间状态都保存起来，只要后续还有数据就可以继续访问

l = my_list()
for i in l:
    print(i)

it = my_list().__iter__()
#it = iter(my_list())
print(it)
print(next(it))
print(it.__next__())
print(next(it))
print(next(it))
print(next(it))