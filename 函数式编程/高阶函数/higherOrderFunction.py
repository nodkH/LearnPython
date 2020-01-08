#!/usr/bin/env python3
#2019年10月31日

###### 高阶函数


#### 变量可以指向函数

print(abs(-10))

print(abs)

x = abs(-10)
print(x)

f = abs
print(f(-19))


#### 函数名也是变量

# abs = 10

# print(abs(-10))


##### 传入函数
def add(x,y,f):
    return f(x) + f(y)

# 这里的f 就是 abs
print(add(-5,-4,f))