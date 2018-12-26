# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Rick Ruan'

with open('ruan_test.txt','a+') as fs:
    fs.write("This is the welcoming speech.\nHello World!")

with open("ruan_test.txt", "r") as fo:
    str = fo.read()
    print(str)
