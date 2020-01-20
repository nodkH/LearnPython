#!/usr/bin/env python3
#2020年1月10日

filePath = '/Users/kongxianggang/Desktop/未命名.txt'

# try:
#     f = open(filePath,'w')
#     f.read()
# finally:
#     if f:
#         f.write('hello wolrd')
#         f.read()
#         f.close()


with open(filePath,'a') as f:
    pass
    f.write('hello pythond')


with open(filePath,'r') as f:
    f.readlines()



