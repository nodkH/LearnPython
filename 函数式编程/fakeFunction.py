#!/usr/bin/env python3
#2019年11月1日


### 匿名函数

l = list(map(lambda x: x * x,[1,2,3]))
print(l)



f = lambda x: x * x
print(f(2))

### 匿名函数作为返回值
def build(x, y):
    return lambda: x * x + y * y

print(build(1,2)())