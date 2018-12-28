# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__='Rick Ruan'
import numpy as np
import pandas as pd
from pandas import Series
from sqlalchemy import create_engine
import time,uuid

def next_id():
    return '%015d%s000' %(int(time.time()*1000),uuid.uuid4().hex)

i=1
ulist=[]
tlist=[]
while i < 4:
    uid = next_id()
    dtime = time.time()
    ulist.append(uid)
    tlist.append(dtime)
    i = i + 1
    time.sleep(3)
    print('Generate uuid&created_time list')
engine = create_engine('mysql+mysqlconnector://data_op:data_op123@localhost:3306/awesome')

dff = pd.DataFrame({"id":ulist,
"email":['Ruan@hotmail.com','Cheng@hotmail.com','Hua@hotmail.com'],
"passwd":['Beijing','Shanghai','Guangzhou'],
"admin":[1, 0, 1],
"name":['100-A','100-B','110-A'],
"image":['/image/0023.jpg','/image/0024.jpg','/image/0025.jpg'],
"created_at":tlist},columns=['id','email','passwd','admin','name','image','created_at'])
print(dff)

#dff.to_excel('Ruan_excel_4.xls')
#dff.to_sql('customer',engine,index=False)
print('Read from and write to Mysql table successfully!')
sql = 'select * from users where 1=1;'
dfq = pd.read_sql_query(sql,engine)
print(dfq)