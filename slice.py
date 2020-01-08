#!/usr/bin/env python3
#2019年10月29日

##### 切片

# 取数组前n个元素

n = ['0','1','2','3','4','5']
y = n[0:3]
print(y)


l = list(range(100))

print(l[-5:])

#隔两个取一个
print(l[::2])

print(l[1::2])

L = l[:]
print(L)


# 元组也是一种list
t = (0,1,2,3,4,5,)
print(t[:3])

# 字符串也是一种list
s = 'abcd'
print(s[0:2])