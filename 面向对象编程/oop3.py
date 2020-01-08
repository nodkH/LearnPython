#!/usr/bin/env python3
#2019年11月18日

### 获取对象信息

import types

print(type(1))

def fn():
    pass

print(type(fn) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)


# 判断是 list,或者是tuple 
print(isinstance([1,2,3],(list,tuple)))


#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir(''))



class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

## 是否有属性 x
print(hasattr(obj,'x'))

## 设置一个属性 y

setattr(obj,'y',19)

print(getattr(obj,'y'))

obj.z = 20

print(obj.z)


## 可以设置默认值，如果不存在该属性的时候，返回默认值
print(getattr(obj,'o',404))


#还可以获取函数名，证明函数也属于属性
print(hasattr(object,'power'))

print(getattr(obj,'power'))

# 给power赋值给变量fn
fn = getattr(obj,'power')

print(fn())





# 小结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

# sum = obj.x + obj.y
# 就不要写：

# sum = getattr(obj, 'x') + getattr(obj, 'y')
# 一个正确的用法的例子如下：

# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。