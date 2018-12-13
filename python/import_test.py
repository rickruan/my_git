# !/usr/bin/env python3
# -*- coding: utf-8 _*_

__author__ = 'Rick Ruan'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello,World!')
    elif len(args)==2:
        print('Hello,',args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
       test()

