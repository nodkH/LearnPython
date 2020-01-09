#!/usr/bin/env python3
#2019年1月9日


### 错误处理

def foo():
    r = some_function()
    if r == (-1):
        return -1
    return r

def bar():
    r = foo()
    if r == (-1):
        print('error')
    else:
        pass


try:
    print('try...')
    r = 10 / 0
    print('result :', r)

except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')

print('end')