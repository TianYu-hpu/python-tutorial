#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#class
#继承
class Base:
    def __init__(self, name="Base"):
        print("init Base")
        self.name = name

    def fun(self):
        print("fun from Base [{}]".format(self.name))

    def fun_2(self):
        print("fun_2 from Base [{}]".format(self.name))

    def funBase(self):
        print("funBase from Base [{}]".format(self.name) )

class A(Base):
    def __init__(self, name="A"):
        #如果这里的super init不加name会怎么样呢
        super().__init__(name=name)
        print("init A")

    def fun(self):
        super().fun()
        print("fun from A [{}]".format(self.name))

    def fun_2(self):
        print("fun_2 from A [{}]".format(self.name))

    def funA(self):
        print("funBase from A [{}]".format(self.name))

class B(Base):
    def __init__(self, name="B"):
        #如果这里的super init不加name会怎么样呢
        super().__init__(name=name)
        print("init B")

    def fun(self):
        super().fun()
        print("fun from B [{}]".format(self.name))

    def fun_2(self):
        super().fun_2()
        print("fun_2 from B [{}]".format(self.name))

    def funB(self):
        print("funBase from B [{}]".format(self.name) )

class DerivedA(A, B):
    def __init__(self, name="DrivedA"):
        #super(DrivedA, self).__init__(name=name)
        #如果这里的super init不加name会怎么样呢
        super().__init__(name=name)
        print("init DrivedA")

    def fun(self):
        super().fun()
        print("fun from DrivedA [{}]".format(self.name))

    def fun_2(self):
        super().fun_2()
        print("fun_2 from DrivedA [{}]".format(self.name))

    def funDrivedA(self):
        print("funBase from DrivedA [{}]".format(self.name))

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