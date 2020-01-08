#!/usr/bin/env python3
#2019年10月23日

#条件判断

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


age = 3

if age>= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


if age:
    print('true')

birth = int(input('birth: '))
if birth >= 2000:
    print('00后')
else:
    print('90后')