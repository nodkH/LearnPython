#!/usr/bin/env python3
#2020年1月16日


import pickle
import json


## 序列化

d = dict(name = 'bob', age = 20, score = 90)

print(pickle.dumps(d))

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f1 = open('dump.txt','rb')
d1 = pickle.load(f1)
f1.close()
print(d1)

## dumps 直接转化为 json 字符串
json.dumps(d1)

## 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

## json字符串---》对象
json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(json.loads(json_str))





# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    
def student2dict(std):
        return {
            'name' : std.name,
            'age' : std.age,
            'score' : std.score
        }
## 对象序列化为json字符串
s = Student('job', 22, 90)
print(json.dumps(s,default=student2dict))


