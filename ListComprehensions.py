#!/usr/bin/env python3
#2019年10月29日

import os

###### 列表生成式

l = list(range(0,10))
print(l)


ll = [x + x for x in range(1,11)]
print(ll)


print([x * x for x in range(1,11) if x % 2 == 0])

# 生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])





