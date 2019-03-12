# -*- coding:utf-8 -*-
import multiprocessing
import time


def add_data(queue):
    for i in range(3):
        print(i)
        queue.put(i)
        time.sleep(0.3)


def read_data(queue):
    while True:
        if queue.empty():
            break
        value = queue.get()
        print(value)


if __name__ == '__main__':
    #创建两个子进程
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    #启动进程执行任务
    add_process.start()
    #进程等待，主进程等待子进程
    read_process.start()


#多任务：使用线程和进程
#从资源角度来说线程更加节省资源
#进程销毁的资源比较多

#从代码的稳定性来说：多进程要比多线程稳定性要强，因为一个进程挂掉不会影响其他进程