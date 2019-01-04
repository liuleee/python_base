# -*- coding:utf-8 -*-
# def show(name,age,*args,**kwargs):
#     print(name,age,args,kwargs)

#不能使用下面的方式进行调用，因为前面使用的关键字后面不能使用位置参数
# show(name='liu',age=18,1,4,c=1,d=2)

# show("lu",20,1,2,3,a = 'apple', b= 'banana')


###  **kwargs必须放在所有参数的最后面
def show(*args,age,name,**kwargs):
    print(name,age,args,kwargs)

    #注意传参顺序，如果前者是args,后面的位置参数需要关键字传参，然后未定义参数的全都给kwargs
show(1,2,name='lu',age=20,aa=1,bb=2)
