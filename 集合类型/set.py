#!/usr/bin/env python3
#2019年10月24日

###### set (无序和无重复元素的集合)



#重复元素会被过滤
s = set([1,2,3,3,3,3])
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)


s1 = set([1,2,3,4,5])
s2 = set([2,5,7,6,8,9])
print(s1 & s2)
print(s1 | s2)

# s3 = set([1,2,3,[4,]])
# print(s3)