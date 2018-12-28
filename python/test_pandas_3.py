# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__='Rick Ruan'
import numpy as np
import pandas as pd
from pandas import Series

dff = pd.DataFrame({"id":[101,102,103,104,105,106],
"date":pd.date_range('20181228', periods=6),
"city":['Beijing','Shanghai','Guangzhou','Shenzhen','Tianjing','Chongqing'],
"age":[23, 44, 54, 32, 34, 32],
"category":['100-A','100-B','110-A','110-C','210-A','130-F'],
"price":[120,np.nan,130,140,np.nan,400]},columns=['id','date','city','category','age','price'])

dff.to_excel('Ruan_excel_3.xls')
dff.to_csv('Ruan_csv_3.csv',sep=',',header=True,index=True)
dff.to_json('Ruan3.json')


print(dff.columns)