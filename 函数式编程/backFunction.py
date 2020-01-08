#!/usr/bin/env python3
#2019年11月1日


##### 返回函数


# 函数作为返回值

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print(calc_sum(1,2,3))




def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4)
print(f)

print(f())




### 闭包

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
