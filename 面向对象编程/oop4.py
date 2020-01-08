#!/usr/bin/env python3
#2019年1月8日


### 实例属性和类属性

class Student(object):
    name = 'Student'
    def __init__(self, name):
        self.name = name


# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。

# 给实例绑定属性的方法是通过实例变量，或者通过self变量：


s = Student('kaixin')
s.score = 90

print(s.name)
print(s.score)

print(Student.name)