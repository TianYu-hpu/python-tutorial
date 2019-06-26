#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#著名的国际象棋比赛的故事
n = 100
count = 0
while n > 0:
    count += n
    n -= 1
else:
    print("end while loop")

print("sum from 1 to 100 is %d" % count)