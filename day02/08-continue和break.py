# -*- coding:utf-8 -*-
#continue结束本次循环，然后可以继续下次循环，整个循环不一定结束


#break:跳出当前循环，当前循环执行结束

#continue和Break不能单独使用，只能在循环语句中使用

# num = 1
# while num < 6:
#     print(num)
#     if num == 2:
#         num += 1
#         #执行continue结束本次循环，continue后面的代码不会执行
#         continue
#     num += 1
# else:
#     print('循环数据结束')

num = 1
while num < 6:
    print(num)
    if num == 2:
        num += 1
        #执行break结束当前循环，break后面的代码不会执行
        break
    num += 1
else:
# 如果循环语句里面执行了break,那么else不会执行
    print('循环数据结束')

print('=========')

# for value in range(1, 5):
#
#     if value == 2:
#         #continue结束本次循环
#         continue
#     print(value)
# else:
#     print('循环结束')

for value in range(1, 5):

    if value == 2:
        #continue结束本次循环
        break
    print(value)
else:
    print('循环结束')

#循环语句里面只要不执行break那么就是执行else语句
result = input('请输入您的姓名：')
for value in ['zhang','lee']:
     if value == result:
         print(value,'here')

         #找到了这个人
         break
else:
    print('no this one')