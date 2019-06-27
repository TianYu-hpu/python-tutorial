#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#generator
class my_list(object):
    def __init__(self):
        self.l = [1,2,3,4]
        #这里用的pop是从后面开始的
        self.l.reverse()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.l) > 0:
            return self.l.pop()
        else:
            raise StopIteration


it = my_list().__iter__()
#it = iter(my_list())
print(it)
print(next(it))
print(it.__next__())
print(next(it))
print(next(it))
print(next(it))