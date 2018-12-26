# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Rick Ruan'

list = []
list.append('Bob chen')
list.append('Rick Ruan')
list.append('Jimmy Xie')
print(list)
print(list[0:3])

del list[1]
print(list)

list.insert(1,'Rick Ruan')
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list.append('Bob chen')
print(list)

list.remove('Bob chen')
print(list)

#list.pop()
#print(list.pop())
#print(list)

list.append('Rick Ruan')
list.append('Bob chen')
print(list)

print(list.index('Rick Ruan'))
print(list.index('Bob chen'))

strline=["Alan T","Hubert xiao","Terry Fan","Joden qiao"]
list.extend(strline)
print(list)
print(len(list))
print(max(list))
print(min(list))
print(list[-2])
print(list[1:])