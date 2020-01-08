#!/usr/bin/env python3
#2019年10月23日

####### dict  字典 键-值（key-value）

d = {'michael' : 99, 'bob' : 80, 'tracy' : 50}
print(d['michael'])


#判断是否存在该key

# 第一种方式，通过 in {}
print('abc' in d)

# 第二种方式，通过get 方法
print(d.get('abc','这个key不存在'))
