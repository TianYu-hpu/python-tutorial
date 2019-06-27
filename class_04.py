#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#class
#继承
class Base:
    def __init__(self, name="Base"):
        print("init Base")

class A(Base):
    def __init__(self, name="A"):
        Base.__init__(self)
        print("init A")

class B(Base):
    def __init__(self, name="B"):
        #如果这里的super init不加name会怎么样呢
        Base.__init__(self)
        print("init B")

class DerivedA(A, B):
    def __init__(self, name="DrivedA"):
        #super(DrivedA, self).__init__(name=name)
        #如果这里的super init不加name会怎么样呢
        A.__init__(self)
        B.__init__(self)
        print("init DrivedA")

da =  DerivedA()
print("*" * 10)
da.fun()
print("*" * 10)
da.fun_2()
print("*" * 10)
da.funA()
print("*" * 10)
da.funB()
print("*" * 10)
da.funDrivedA()