#!/usr/bin/env python3
#2019年10月31日


#### filter (也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。)

def is_odd(n):
    return n % 2 == 1


l = list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))

print(l)


def not_empty(s):
    return s and s.strip()

l1 = list(filter(not_empty,['A','','B',None,'C','']))

print(l1)




#### 用filter求素数

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it) # 构造新序列


for n in primes():
        if n < 10:
            print(n)
        else:
            break


