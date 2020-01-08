#!/usr/bin/env python3
#2019年10月30日

from collections import Iterable
from collections import Iterator

#### 迭代器  可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。


# 凡是可作用于for循环的对象都是Iterable类型；   （可迭代的）

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# Python的for循环本质上就是通过不断调用next()函数实现的

print(isinstance([],Iterable))

print(isinstance({},Iterable))

print(isinstance('abc',Iterable))

print(isinstance((x for x in range(10)), Iterable))

print(isinstance(100,Iterable))


print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({},Iterator))