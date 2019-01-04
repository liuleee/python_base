# -*- coding: utf-8 -*-

#定义不可变类型全局变量
# g_num = 10
# print(id(g_num))
# def modify():
#     #声明要修改全局变量，表示要修改全局变量的内存地址
#     global g_num
#     g_num = 1
#     print('modify:',id(g_num))
#
# modify()


#定义可变类型的全局变量
g_list = [3,5]
print(id(g_list))
def modify():
# 在原有数据的基础上添加数据
    #global g_list    ###加上global表示内存地址要发生改变
    g_list.append(4)
    # g_list = [1,4]
    print('modify:',g_list)
    print('modify:id',id(g_list))

modify()
