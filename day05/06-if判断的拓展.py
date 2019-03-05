# -*- coding:utf-8 -*-
#if判：bool,数字，容器（字符串，列表，元组，字典，集合），None(空值）
if True:
    print('条件成立')
#数字类型：非o即真，只要不是0就是成立的
if 1:
    print('success!')
# if 0:
#     print('success!')
#容器判断的时候，如果容器类型里面有数据那么表示条件成立，否则条件不成立
if "xxx":
    print("ddd")
if [1,2]:
    print('nnnnn')
if {'name':'liu'}:
    print('dddd')
#非None条件成立，None表示条件不成立
if not None:
    print('mmmmmm')