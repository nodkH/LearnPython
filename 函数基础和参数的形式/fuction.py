#!/usr/bin/env python3
#2019年10月24日

#### 函数

def firstFuction(parameter):
    print(parameter)


firstFuction([4,])


# 空函数
def noneFuction():
    pass


noneFuction()



# 类型检查

def function2(parameter):
    if not isinstance(parameter,(int,str)):
        raise TypeError('类型不正确')
    print(parameter)


function2('4')



def move(x,y,h=0):
    return x,y,h


print(move(1,2,3))



# def power(x):
#     return x * x


# print(power(5))


def power(x,n = 2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
        
    
    return s


print(power(5,3))


print(power(5))


def addEnd(L=[]):
    L.append('end')
    return L

# print(addEnd([1,3,4]))
# print(addEnd([1,3,4,5]))
# print(addEnd([1,3,4,6]))

print(addEnd([]))
# print(addEnd([]))
# print(addEnd([]))
# print(addEnd([]))
# print(addEnd([]))
# print(addEnd([]))



#### 可变参数  传入一个元组

def calc(*numers):
    print(numers)

calc(1,2,'3',4)


#### 关键字参数  可选填的参数
def person(name,age,**kw):
    if 'city' in kw:
        pass

    if 'job' in kw:
        pass

    print('name',name,'age',age,'other',kw)


person('kong',25)

person('kong',25,addr='qingdao')

dict = {'addr' : 'qingdao', 'job' : 'enginer'}
person('kong', 25, **dict)


### 声明必须带有必要参数的函数
def person1(name, age, *, city, job):
    print(name,age,city,job)


person1('kongxg', 25, **{'city' : 'qingdao', 'job' : 'enginer'})


### 如果必要参数前面，已经有可选参数列表的形式
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


person2('kxg', 25, '可选',  **{'city' : 'qingdao',  'job' : 'enginer'})





 
#### 参数组合

def f1(a, b, c = 0, *args, **kw):
    print(a, b , c, args, kw)


def f2(a, b, c = 0, *, d, **kw):
    print(a, b, c, d, kw)

f1(1,{'a' : '000'})
f2(1, 2, 3 , d=99, ext=None)










#### 递归函数


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print("5的阶乘=",fact(5)) 

print(list(range(1,100,2)))


