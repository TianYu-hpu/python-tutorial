#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#generator
l = [1,2,3,4]
#it = l.__iter__()
it = iter(l)
print(it)
print(next(it))
print(it.__next__())
print(next(it))
print(next(it))
print(next(it))