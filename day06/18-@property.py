# -*- coding:utf-8 -*-
#把方法改成属性
class Student(object):
    def __init__(self):
        self.__score = 100

     # 获取值
    @property
    def get_score(self):
        return self.__score
    # 设置值
    @get_score.setter
    def set_score(self, score):
        self.__score = score


stu = Student()
# score = stu.get_score()
# print(score)
#
# stu.set_score(200)
# score = stu.get_score()
# print(score)
#
# stu.set_score = 99

score = stu.get_score
print(score)

stu.set_score = 80
score = stu.get_score
print(score)