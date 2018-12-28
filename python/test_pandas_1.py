# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__='Rick Ruan'
import numpy as np
import pandas as pd
from pandas import Series

stus = [['姓名','年龄','性别','分数'],
    ['Mary',20,'女',90],
    ['Gracy',40,'女',90.5],
    ['Jodan',25,'男',98],
    ['MaryLy',20,'女',100]
    ]

slt1 = Series(data=[1,2,3,4,5,6,7,8])
print(slt1)

slt2 = Series(data=np.linspace(0,10,3))
print(slt2)

slt3 = Series(data=np.random.randint(1,50,size=(3)),index=['语文','数学','英语'])
print(slt3)

dlist = {'Python':90, 'Java':98, 'C++':70}
slt4 = Series(data=dlist)
print(slt4)
print(slt4['Python'])
print(slt4[['Python','Java','C++']])