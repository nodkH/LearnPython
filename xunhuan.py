#!/usr/bin/env python3
#2019年10月23日

####### 循环

names = ('james', 'micale', 'jobs')

for name in names:
    print(name)

sum = 0

for value in list(range(101)):
    sum += value

print(sum)


n = 0

while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    # if n == 10:
    #     break
    print(n)
    
print('end')