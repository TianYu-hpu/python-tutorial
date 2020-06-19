#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
print(os.getcwd())
import packageimport_02 as module2

def main():
    print("main function in module2.__main__")
    fun()

def fun():
    print("fun in module2 __main__")
    print("invoke module2.fun")
    module2.fun()

var1 = 789
var2 = "hij"

print("this is module2 __main__")
if __name__ == "__main__":
    main()

