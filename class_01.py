#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#class
class Greeter:
    #类属性
    member = "Greeter"

    def __init__(self, name):
        #实例属性
        self.name = name

    #实例方法
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

        #类方法，需要通过classmethod进行定义
        @classmethod
        def Greet(cls, loud=True):
            '''
            这里的cls是调用这个方法的类
            :param cls:
            :param loud:
            :return:
            '''
            print("cls is :[{}]".format(cls))
            if(loud):
                print("HELLO, %s!" % cls.member.upper())
            else:
                print("Hello, %s!" % cls.member)

g = Greeter("Fred")
g.greet()
g.greet(loud=True)

#类的方法可以通过类来调用，也可以通过实例调用
Greeter.Greet()
g.Greet()

#类属性可以通过实例或者类本身读取
print(g.member)
print(Greeter.member)

g.member = 'greeter'
#但是直接在实例上复制会创建一个新的实例属性，而不是修改类属性的值
#所以如果用实例调用类方法，而里面又设计了对类的属性的修改，就会出问题
print(g.member)
print(Greeter.member)
