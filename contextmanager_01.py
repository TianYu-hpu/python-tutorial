#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#context manager中最重要的是__enter__和 __exit__两个方法，
# 这个两个方法分别用于处理资源的初始化和资源的清理，实现这两个方法并
# 适当的处理资源就可以了

class my_open:
    def __init__(self, path, suppress = False):
        self.path = path
        self.suppress = suppress

    def read(self):
        return self.f.read()

    def fail(self):
        print("try raise a error")
        raise ValueError

    def __enter__(self):
        '''
        enter可以返回self或者其他什么东西
        在with语法中，如果有as,那么这里返回的内容会被绑定到as后面的变量上面
        :return: 
        '''
        print("starting with block")
        self.f = open(self.path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        如果在context manager运行的过程中出现了异常，那么异常会被传入exit作为判断的依据
        exit返回False则认为context manager失败了，这些异常会被直接重新抛出
        但是如果exit里面处理了这些异常，而且反馈了一个True，那么这些异常讲不会在向外传递
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        '''

        self.f.close()

        if exc_type is None:
            print("exited normally\n")
        else:
            print("raise an exception!" + str(exc_type))

        return self.suppress

with my_open("/tmp/test.txt") as f:
    print(f.read())

try:
    with my_open("/tmp/test.txt") as f:
        f.fail()
except ValueError:
    print("ValueError raised")

try:
    with my_open("/tmp/test.txt", suppress=True) as f:
        f.fail()
except ValueError:
    print("ValueError raised")




