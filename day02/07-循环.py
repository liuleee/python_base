# -*- coding:utf-8 -*-
#循环（for,while):根据条件循环执行某种操作
#提示：while会循环判断条件是否成立，如果条件成立会执行while循环语句，但if只会判断一次
num = 1
while num < 6:
    print(num)
    num += 1



#for循环一般会结果range使用，range是一种范围
# for value in range(1,6):
    # print(value)

#for和while可以结合else语句使用

#循环结束后执行else语句

#break相当于执行当前操作
num = 5
while num > 1:
    if num==4:
        print('num ==4 ok')
    print(num)
    num -= 1
else:
    print("循环结束")

print('========')



