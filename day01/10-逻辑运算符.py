# -*- coding: utf-8 -*-
#逻辑运算符 and   or   not

score = 90


#and表示左右两边条件都成立
if score >=90 and score <= 100:
    print("优秀")
else:
    print('不优秀')


#or表示左右两边条件有1个成立就执行
num1 = 1
if num1 == 1 or num1 == 2:
    print("执行我")

#
#not对结果进行取反，not对False进行取反就是True
if not 1 == 2:
    print('能执行吗')