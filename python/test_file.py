# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

with open('test.txt','w') as f:
    f.write('\n\nToday is\\\t')
    f.write(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

with open('test.txt','r') as f:
    s = f.read()
    print('open test.txt for read...')
    print(s)

with open('test.txt','rb') as f:
    s = f.read()
    print('open test.txt as binary for read...')
    print(s)
