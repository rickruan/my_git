# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Rick Ruan'

class Stduent(object):

    @property
    def score(self):
        return self._score 

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('Score must be an integer!')
        if value<0 or value>100:
            raise ValueError('Score must between 0~100!')
        self._score=value
 
s=Stduent()
s.score=90
print('s.score=',s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999
