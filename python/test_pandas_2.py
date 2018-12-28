# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__='Rick Ruan'
import numpy as np
import pandas as pd
from pandas import Series

dff = pd.DataFrame(pd.read_excel('Ruan_excel_1.xls'))

print(dff.loc[3])
print(dff.head(4))
print(dff.tail(2))
print(dff.columns)

dff.index=['1', '2', '3', '4']
dff.columns=['姓名', '年龄', '性别', '分值']
dff.to_excel('Ruan_excel_2.xls')
dff.to_csv('Ruan_csv_1.csv',sep=',',header=True,index=True)
dff.to_json('Ruan.json')

print(dff.columns)