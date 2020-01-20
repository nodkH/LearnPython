#!/usr/bin/env python3
#2019年1月10日

import logging

logging.basicConfig(level=logging.INFO)


### 调试

###  虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。


### 断言

# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。



# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n

# foo('0')


s = '0'

n = int(s)

logging.info('n = %d' % n)
print(10 / n)


s1 = '0'
n1 = int(s1)

print(10 / n1)
