# !/usr/bin/env python3
# -*- coding: utf-8 _*_

__author__='Rick Ruan'

class Stduent(object):
    name='Stduent'
    def __init__(self,name):
        self.name=name

s=Stduent('Bob')
s.score=90

print('stduent\'s name is',s.name)
print('stduent\'s attr name is',Stduent.name)
s.name='Michael'
print('stduent\'s name is',s.name)
print(Stduent.name)
del s.name
print(s.name)
