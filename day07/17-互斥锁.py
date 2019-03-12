# -*- coding:utf-8 -*-
import threading
#互斥锁
#创建互斥锁
lock = threading.Lock()
g_num = 0
def AA():
    #上锁
    lock.acquire()
    global g_num
    for i in range(100000):
        g_num += 1
    print("AA:",g_num)
    #释放锁
    lock.release()

def BB():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(100000):
        g_num += 1
    print("BB:",g_num)
    # 释放锁
    lock.release()

if __name__ == "__main__":
    #创建两个线程
    first_thread = threading.Thread(target=AA)
    second_thread = threading.Thread(target=BB)

    first_thread.start()
    second_thread.start()