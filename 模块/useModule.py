#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2019年11月5日


'a test module' #任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'kong xiang gang' #使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

import sys
# import numpy

## 前面加下划线，代表私有的
def _private(name):
    return 'hello, %s' %name


def test():
    #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello, %s!'% args[1])
    else:
        print('too many arguments!')
    

# print(sys.path)

## 可以用来判断是直接运行的这个类，还是被其他文件导入了
## 如果是其他类导入了，不会执行
if __name__ == '__main__':
    test()
    print(_private('kxg')) 



