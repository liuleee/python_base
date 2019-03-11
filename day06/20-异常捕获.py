# -*- coding:utf-8 -*-

# try:#可能出现异常的代码放在try语句里面
#     num1 = int(input("请输入一个数字"))
#     num2 = int(input("请输入一个数字"))
#
#     result = num2+num1
#     print(result)
#
# except Exception as e: #e表示异常对象
#     #捕获到的异常会在except里面进行处理
#     print("请输入合法的数字")
#     print(e,type(e))


#提示：多数异常类都是继承Exception

#了解：可以捕获多个异常类型
# try:
#     name = "zs"
#     def name
#     print(name)
#
# # 在try里面如果执行了异常那么不会执行try语句里面的代码，会执行exception
#     result = 1 / 0
#     print(result)
#
# except Exception as e:
#     print(e,type(e))


# 没有异常
try:


# 在try里面如果执行了异常那么不会执行try语句里面的代码，会执行exception
    result = 1 / 1
    print(result)

except Exception as e:
    print("出现异常")
else:
    print("没有异常")
finally:
    print("有没有异常都要执行")
