#!/usr/bin/env python3
#2019年10月31日

from functools import reduce

###### map / reduce




#### map (map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回)


def f(x):
    return x * x

for n in map(f,[1,2,3,4,5,6]):
    print(n)


## map 转换出来的是 Iterator 迭代器 是惰性序列，所以用 list()列表生成式
print(list(map(f,[1,2,3,4,5,6])))

## 一句话转换为字符串list
print(list(map(str,[1,2,3,4,5,6])))




##### reduce  (reduce把结果继续和序列的下一个元素做累积计算)

def add(x,y):
    return x + y

print(reduce(add,[1,2,3,4,5]))



def fn(x,y):
    return x * 10 + y

def char2num(s):
    digits = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
    return digits[s]

### 把字符串转换为整数
print(reduce(fn, map(char2num, '13456')))


### string2int的函数就是：
DIGITS = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    
    def char2num(s):
        return DIGITS[s]
    
    return reduce(fn, map(char2num,s))





print(str2int('45643'))


