# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

#write to stringio

f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World!')
print(f.getvalue())

#read from stringio

f=StringIO('What are you doing!\nVery Fine\nGoodbye!')
while True:
    s=f.readline()
    if s == '':
        break
    print(s.strip())
