#!/usr/bin/env python3
#2019年11月18日

##继承和多态
# 小结
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

class Animal(object):
    def run(self):
        print('animal can run')

    def hh(self):
        pass



class Dog(Animal):
    def run(self):
        print('dog can run')
    pass

class Cat(Animal):
    def run(self):
        print('cat can run')
    pass



dog = Dog()
# dog.run()

def run_twice(animal):
        animal.run()
        animal.run()

run_twice(dog)


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
    pass



run_twice(Tortoise())


class likeClass(object):
    def run(self):
        print('like this')
    pass


run_twice(likeClass())



# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

# class Timer(object):
#     def run(self):
#         print('Start...')
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。




