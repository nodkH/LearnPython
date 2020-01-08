#!/usr/bin/env python3
#2019年10月23日

######### tuple 元组 (不可变有序集合)

# tuple 不可变
classmates = ('michael', 'Bob', 'Tracy')
print(classmates)

t = (1,2)
print(t)

t = ()
print(t)

#如果想定义只有一个元素的元组，需要在后面加一个逗号
t = (1,)
print(t)


t = ('a','b',[1,2])
t[2][0] = 'x'
t[2][1] = 'y'
print(t)
