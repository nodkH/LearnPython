#!/usr/bin/env python3
#2019年10月23日


print(2+3)
print('hello python')
print('duo','ge','zi','fu','chuan')
name = 'kong xiang gang'
print('名字是:',name)

############## list (可变有序集合)


classmates = ['michael', 'bob', 'tracy']
print(classmates)

#数组越界
# print(classmates[3]) 
print(classmates[-1])

print(classmates[-2])
print(classmates[-3])
#同样越界
# print(classmates[-4])


#添加到末尾
classmates.append('Adam')
print(classmates)
#插入到指定位置
classmates.insert(1,'jack')
print(classmates)

#删除末尾的元素
classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

L = ['apple',123,True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

print(s[2][1])


