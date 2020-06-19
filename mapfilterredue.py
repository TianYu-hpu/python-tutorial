#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#map,filter,reduce
list = [1,2,3,4,5,6,7,8,9,10]

l_square = [e ** 2 for e in list]
print(l_square)
#注意map返回的是一个map object,需要用list去run一下
list_square = list(map(lambda e: e ** 1, list))
print(list_square)

#map接受的函数对sequence的每个元素操作并返回操作后的结果，map本身产生一个generator,用list可以取得generator的结果
#把这个list里面的所有偶数找出来
l_square = [e for e in list if e % 2 == 0]
print(l_square)

l_square = list(filter(lambda e: e % 2 == 0, list))
print(l_square)

print(sum(list))

#相比与map/filter/reduce没那么常用，所以诶放在了functools
from functools import reduce
'''
reduce最特殊，他会接受一个有两个输入的函数，两个输入会在这个函数里面进行一定的运算，
返回一个值，而这个值会被用来跟这个sequence的下一个值继续进行运算，知道所有的sequence元素都
被处理完，reduce不会返回generator,而是直接翻坠最终值
'''
print(reduce(lambda x, y : x+y, list))


'''
help(map)
help(filter)
help(reduce)
'''

start = "characters of input string are:"
string = "hello, world"

print(reduce(lambda x, y + x +"[{}]".format(y), string, start))





