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


#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。




# 使用__slots__

#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class Student2(object):
    ## 只允许定义的属性
    __slots__ = ('name','age')
    pass

s1 = Student2()
s1.name = 'ddd'
# s1.score = 90