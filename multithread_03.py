#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#GIL(Global interpreter lock)
from threading import Thread
import time

class myThread(Thread):
    def run(self):
        for i in range(2):
            print("child process is working")
            time.sleep(1)

my_thread = myThread()
#不是调用run,而是调用这个start去启动一个线程
my_thread.start()

print(my_thread.is_alive())

my_thread.join()

#等待子线程退出，如果没有这一句，那么主线程退出就会直接干掉子线程
#不过我们这里是一个python交互shell里面，最高主线程会一直存在
print("child process exited")


