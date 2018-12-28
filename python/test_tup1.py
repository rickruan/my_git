# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__='Rick Ruan'

tup1 = (11, 22, 33)
tup2 = ('aa', 'bb', 'cc')
print(tup1)
print(tup2)

tup1 += tup2
print(tup1)
print(tup2)

list1 = [1, 2, 3, 4, 5]
print(list1)
tup3= tuple(list1)
print(tup3)

list2=list(tup3)
print(list2)
