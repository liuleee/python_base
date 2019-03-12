# -*- coding:utf-8 -*-
import multiprocessing
import time
my_list = []
def add_data():
    for i in range(3):
        my_list.append(i)

    print("add_data:",my_list)

def read_data():
    print("read:",my_list)

if __name__ == '__main__':
    #创建两个子进程
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    #启动进程执行任务
    add_process.start()
    #进程等待，主进程等待子进程
    read_process.start()