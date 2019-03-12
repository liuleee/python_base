# -*- coding:utf-8 -*-
import time
import threading
def AA(count):
    print("AA:",threading.current_thread())
    print("这个代码是在子线程中执行的")
    # for i in range(count):
    while True:
        print("AA")
        time.sleep(0.2)
#测试
if __name__ =='__main__':
    print("main:", threading.current_thread())
    #target指定的目标函数是在子线程中执行
    sub_thread = threading.Thread(target=AA,args=(5,),daemon=True)
    #设置守护线程,主线程推出子线程直接销毁不在执行对应的代码
    # sub_thread.setDaemon(True)
    sub_thread.start()

    time.sleep(1)
    print("over")


#总结：主线程会等到子线程执行完成以后，程序再退出
