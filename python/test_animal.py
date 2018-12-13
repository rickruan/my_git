#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__='Rick Ruan'

class Animal(object):
    def run(self):
        print('Animal is running....')

class Dog(Animal):
    def run(self):
        print('Dog is running....')

class Cat(Animal):
    def run(self):
        print('Cat is running....')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
b = Dog()
c = Cat()

print('a is Animal?',isinstance(a,Animal))
print('a is Dog?',isinstance(a,Dog))
print('a is Cat?',isinstance(a,Cat))

print('b is Animal?',isinstance(b,Animal))
print('b is Dog?',isinstance(b,Dog))
print('b is Cat?',isinstance(b,Cat))

run_twice(c)
