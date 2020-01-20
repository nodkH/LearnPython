#!/usr/bin/env python3
#2020年1月20日


### 多进程

import os

# print('process (%s) start...' % os.getpid() )

pid = os.fork()

if pid == 0:
    print('i am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid))
else:
    print('i (%s) just created a child process (%s).' % (os.getpid(), pid))
