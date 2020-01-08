#!/usr/bin/env python3
#2019年10月29日

from collections import Iterable

##### 迭代

d = {'a' : 1, 'b' : 2 , 'c' : 3}

for k , v in d.items():
    print('k=', k + ' ' + 'v=',v)


# 字符串是可迭代的
print(isinstance('123', Iterable))
# 整数类型是不可迭代的
print(isinstance(123, Iterable))

for index, value in enumerate([(1,2), (3,4), (5,6), (7,8)]):
    print(index,value)


for index, value in enumerate(['1','2','3','4','5']):
    print(index,value)