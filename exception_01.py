#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Exception handler
a = 1
b = 0
try:
    c = a / b
except
    print("Failed, but i dont't know why!")

try:
    c = a / b
except Exception as  ex:
    print("failed, dont know what type this exception is but I gang the the detail:[{}]".format(ex))

try:
    c = a / b
except ZeroDivisionError:
    #明确知道错误原因，但是不知道细节
    print("failed, caused by ZeroDivisionError but I gang the the detail")


try:
    c = a / b
except ZeroDivisionError as ex:
    #明确知道错误原因，但是不知道细节
    print("failed, caused by ZeroDivisionError but I gang the the detail:[{}]".format(ex))


try:
    c = a / NotExist
except ZeroDivisionError as ex:
    #明确知道错误原因，但是不知道细节
    print("failed, caused by ZeroDivisionError but I gang the the detail:[{}]".format(ex))
except:
    print("failed, not caused by ZeroDivisionError, I don't know why")

try:
    c = a / NotExist
except ZeroDivisionError as ex:
    #明确知道错误原因，但是不知道细节
    print("failed, caused by ZeroDivisionError but I gang the the detail:[{}]".format(ex))
except NameError as ex:
    print("failed, not caused by NameError, I don't know why, [{}]".format(ex))


try:
    c = a / NotExist
except ZeroDivisionError as ex:
    #明确知道错误原因，但是不知道细节
    print("failed, caused by ZeroDivisionError but I gang the the detail:[{}]".format(ex))
except NameError as ex:
    print("failed, not caused by NameError, I don't know why, [{}]".format(ex))
except:
    print("failed,  I don't know why")
finally:
    print("failed or not, this line will be run")

try:
    raise OSError
except ZeroDivisionError as ex:
    #明确知道错误原因，但是不知道细节
    print("failed, caused by ZeroDivisionError but I gang the the detail:[{}]".format(ex))
except NameError as ex:
    print("failed, not caused by NameError, I don't know why, [{}]".format(ex))
except:
    print("failed,  I don't know why")
finally:
    print("failed or not, this line will be run")

try:
    raise OSError("dont know what to do, how about raise a exception")
except ZeroDivisionError as ex:
    #明确知道错误原因，但是不知道细节
    print("failed, caused by ZeroDivisionError but I gang the the detail:[{}]".format(ex))
except NameError as ex:
    print("failed, not caused by NameError, I don't know why, [{}]".format(ex))
except:
    print("failed,  I don't know why")
finally:
    print("failed or not, this line will be run")

try:
    c = int("ttt")
except ZeroDivisionError as ex:
    #明确知道错误原因，但是不知道细节
    print("failed, caused by ZeroDivisionError but I gang the the detail:[{}]".format(ex))
except NameError as ex:
    print("failed, not caused by NameError, I don't know why, [{}]".format(ex))
except:
    print("failed,  I don't know why")
    raise
finally:
    print("failed or not, this line will be run")






