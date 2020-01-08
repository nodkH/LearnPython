#!/usr/bin/env python3
#2019年11月1日


### 装饰器 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def now():
    print('2019-11-1')

f = now

f()

print(f.__name__)


## log
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now1():
    print('2015-3-2')

# @语法 就相当于 now1 = log(now1)
# now1 = log(now1)

now1()


