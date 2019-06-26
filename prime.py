#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#素数
from math import sqrt

for i in range(1000):
    if i % 2 == 0:
        #偶数
        print("{} is a even numer".format(i))
    elif i % 2 != 0:
        #只针对奇数判断素数，偶数肯定是合数
        for j in range(2, int(sqrt(i) + 1)):
            if i % j == 0:
                #能被1和自己之外的数字整除，合数，后续计算没必要进行下去了
                print("{} is a composite numer".format(i))
                break
        else:
            print("{} is a prime numer".format(i))

        print("{} is a odd numer".format(i))

    else:
        print("this not even possible for{}".format(i))