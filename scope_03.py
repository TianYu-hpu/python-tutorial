#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#作用域
for i in range(10):
    inner_var2 = i +1
    print(inner_var2)

print(inner_var2)

a = 1
if a > 0:
    inner_var = 2
else:
    inner_var = 4

'''
    这里，inner_var是在if语句中定义的，但是在if语句外面，这个变量仍然可以访问
    同样的情况发生在for,while循环中
'''
print(inner_var)

'''
这里的inner_var2用的是上面的for循环中定义的inner_var2,而不是if语句中的，如果没有上面的for
循环，这里应该是要报错的

这是一种比较常见的问题，循环结束后，没有确认就重用了循环里面的变量
'''
print(inner_var2)


#end 各语句不能形成变量作用于，只有函数和class能够形成变量作用域

