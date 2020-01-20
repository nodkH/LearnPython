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
    r = 10 / 0                  #除法错误
    print('result :', r)        #不会向下执行

except ZeroDivisionError as e:  #捕获到错误
    print('except:', e)

except ValueError as e:         #可以捕获多种类型的错误
    print('Value Error:', e)

else:
    print('no error!')          #没有错误时，会执行else

finally:
    print('finally...')

print('end')



def foo1(s):
    return 10 / int(s)

def bar(s):
    return foo1(s) * 2


try:
    bar('0')

except Exception as e:
    print('error:' , e)

finally:
    print('finally')



