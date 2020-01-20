#!/usr/bin/env python3
#2020/1/10

import os

#### 文件和文件夹的操作


print(os.name)  ## 操作系统类型     如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。


## 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

print(os.uname()) # 要获取详细的系统信息，可以调用uname()函数：

print(os.environ)


# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.join('/Users/kongxianggang/Desktop/python','testdir'))

## 然后创建一个目录:
# os.mkdir('/Users/kongxianggang/Desktop/python/testdir1')

# 删掉一个目录
# os.rmdir('/Users/kongxianggang/Desktop/python/testdir1')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：


# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名

print(os.path.split('/Users/kongxianggang/Desktop/python/testdir1'))

