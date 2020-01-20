
#!/usr/bin/env python3
#2020/1/10


# StringIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。

# StringIO顾名思义就是在内存中读写str。

# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：


from io import StringIO, BytesIO

# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world')

# print(f.getvalue())



f = StringIO()
f = StringIO('hello \nhi\ngood bye')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


f1 = BytesIO()
f1.write('中文'.encode('utf-8'))
print(f1.getvalue())