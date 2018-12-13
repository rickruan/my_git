# !/usr/bin/env python3
# -*- coding: utf-8 _*_

__author__='Rick Ruan'

class student(object):
    def __init__(self,name,gender):
        if gender in ('male','female'):
           self.__gender=gender
        else:
           raise ValueError('gender is input error!')
           self.__name=name
    def set_gender(self):
        gender=input('pls input gender:')
        if gender in ('male','female'):
           self.__gender=gender
        else:
           raise ValueError('gender is wrong!')
    def get_gender(self):
        return self.__gender

std = student('Jack','male')
print('Student test is success,',std.get_gender())
