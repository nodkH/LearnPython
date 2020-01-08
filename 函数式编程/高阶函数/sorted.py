#!/usr/bin/env python3
#2019年10月31日


#### sorted （排序）


l = sorted([1,99,abs(-994),-4,0])
print(l)


### sorted 也是一个高阶函数，可以接受一个key函数来实现自定义排序
print(sorted(l,key=abs))

list = [36, 5, -12, 9, -21]
keys = [36, 5, 12, 9, 21]

# print(sorted(list,key=keys))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))



print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))
