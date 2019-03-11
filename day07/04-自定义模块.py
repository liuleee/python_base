# -*- coding:utf-8 -*-
# 自定义模块名字和变量名的定义很类似，都是由字母、数字、下划线组成，不能以数字开头，否则无法导入该模块
# 模块名的命名规则与变量名一样，使用下划线命名法

# import test_module
import test1_module



# print(test_module.g_num)
# test_module.show()
# stu = test_module.Student("李四",30)
# print(stu.show_msg())

result = test1_module.sum_num(3,2)
print("自定义模块：",result)
#查看模块名
print(__name__)