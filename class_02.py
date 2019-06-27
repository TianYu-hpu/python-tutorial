#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#class
class Greeter3:
    def __init__(self, name):
        #实例属性
        self.name = name

#独立于类定义的一个函数定义
def greet(self, load=False):
    '''
    这里的self是调用这个方法的本类的实例
    :param load:
    :return:
    '''
    print("self is :[{}]".format(self))

    if load:
        print("HELLO, %s!" % self.name.upper())
    else:
        print("Hello, %s!" % self.name)


#函数的定义可以在运行的时候被替换
Greeter3.greet = greet
g = Greeter3("Greeter3")
g.greet()
g.greet(load = True)


