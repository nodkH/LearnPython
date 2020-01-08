#!/usr/bin/env python3
#2019年1月8日

from types import MethodType

class Student(object):
    pass

s = Student()
s.name = 'michael'
print(s.name)



def set_age(self,age):
    self.age = age


def set_score(self,score):
    self.score = score



# 给实例绑定一个方法
s.set_age = MethodType(set_age,s)

s.set_age(25)

print(s.age)

s2 = Student()
# 只能对特定的实例起作用
# s2.set_age(24)


# 给class绑定方法
Student.set_score = set_score

# 给class绑定的方法，所有实例都能调用
s.set_score(100)
s2.set_score(101)
