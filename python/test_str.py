# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Rick Ruan'

class Stduent(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Stduent object(name: %s)' %self.name
    __repr__ = __str__
print(Stduent('Michael'))

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __inter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 100000:
           raise StopInteration();
        return self.a

for n in Fib():
    print(n)
