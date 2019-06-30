#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
当代码比较少的时候，运行一个python shell, 一个jupyter,或者单单在一个python文件就能解决，
一旦系统上了一定的过，代码量比较大的时候，代码的组织管理就会变成一个足够影响整个项目的开发进度效率
甚至是项目生死的至关重要的问题

一个python文件就是一个module,可以被import,像内建的module一样被调用

一个目录，如果其下面包含一个__init__py文件的话，这个目录就是一个package,目录下的所有py文件都是这个
package的成员，目录下如果还有子目录的话，仍然是__init__.py的为子package,没有的只是普通文件夹

__init__.py文件可以为空，但是我们一般都是在里面放一些初始化的代码

如果要把这个package作为一个module,直接运行的话，这个目录下，还需要有一个__main__.py文件
'''
def main():
    print("main function in module a")

def fun():
    print("fun in module a")

var1 = 12345
var2 = "abcd"

print("this is module a!")

if __name__ == "__main__":
    main()




