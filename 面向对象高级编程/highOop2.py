#!/usr/bin/env python3
#2019年1月8日

#### 使用   @property

class Student(object):
    # def get_scroe(self):
    #     return self._score

    # def set_scroe(self,score):
    #     if not isinstance(score,int):
    #         raise ValueError('score must be a int')
    #     if score < 0 or score > 100:
    #         raise ValueError('score must between 0-100')
    #     self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be a int')
        if score < 0 or score > 100:
            raise ValueError('score must between 0-100')
        self._score = score

s = Student()
# s.set_scroe(99)
# print(s.get_scroe())
# s.set_scroe(1001)

s.score = 99
print(s.score)

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性

