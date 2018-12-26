# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Rick Ruan'

import time,uuid
from datetime import datetime

def next_id():
    return '%015d%s000' %(int(time.time()*1000),uuid.uuid4().hex)

import mysql.connector
conn = mysql.connector.connect(user='data_op',password='data_op123',database='awesome')

uid = next_id()
dtime = time.time()
admin = 1
user_1 = ['ruanchenghua@hotmail.com','ruan123','Rick','/image/0011.png']
cur = conn.cursor()
sql = "insert into users(id,email,passwd,admin,name,image,created_at) VALUES('%s','%s','%s','%d','%s','%s','%f')" %(uid,user_1[0],user_1[1],admin,user_1[2],user_1[3],dtime)
cur.execute(sql)
conn.commit()
cur.close()

cursor = conn.cursor()
cursor.execute('select * from users where name = %s', ('Rick',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()