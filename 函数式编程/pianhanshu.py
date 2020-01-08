#!/usr/bin/env python3
#2019年11月4日

import functools

### 偏函数  简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

int2 = functools.partial(int,base=2)

print(int2('10000'))

int2('1000')
#相当于：固定了int()函数的关键字参数base

# 也就是 相当于

kw = {'base' : 2}
int('1000',**kw)