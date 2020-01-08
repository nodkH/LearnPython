#!/usr/bin/env python3
#2019年10月30日

#### 生成器

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))


for n in g:
    print(n)

print("##################1")

def fib(max):
    n, a, b = 0,0,1
    while n < max:
        yield b
        a , b = b, a + b
        n += 1
    return 'done'

f = fib(6)
print(next(f))


# for b in f:
#     print(b)


while True:
    try:
        x = next(f)
        print('f:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break



print('#########')

def odd():
    print('step 1')
    yield 1

    print('step 2')
    yield 3

    print('step 3')
    yield 5



o = odd()

print(next(o))

print(next(o))