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
    def set_gender(self,gender):
        gender=input('pls input gender:')
        if gender in ('male','female'):
           self.__gender=gender
        else:
           raise ValueError('gender is wrong!')
    def get_gender(self):
        return self.__gender


stdent=student('Jackie','male')
if stdent.get_gender() != 'male':
    stdent.set_gender('female')
    print('Student test is fail,',stdent.get_gender())
else:
    stdent.set_gender('male')
    print('Student test is success,',stdent.get_gender())
