# -*- coding:utf-8 -*-
#生成器是特殊的迭代器，也就是说它可以通过next函数和for循环取值
#迭代器和生成器的好处是：根据每次生成一个值，不像列表把所有数据都准备好，这样列表比较占用内存

#1.使用生成器的表达式创建
# result = [x for x in range(4)]
# print(result,type(result))

# result = (x for x in range(4))
# print(result)

#测试：使用next获取下一个值
# value = next(result)
# print(value)
# for value in result:
#     print(value)


#2.使用yeild创建生成器
def show_num():
    for i in range(5):
        # return i
        yield i

g = show_num()
# value = next(g)
# print(value)
for value in g:
    print(value)