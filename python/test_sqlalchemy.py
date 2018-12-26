# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Rick Ruan'

from sqlalchemy import Column,String,create_engine
from sqlalchemy.types import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time,uuid

def next_id():
    return '%015d%s000' %(int(time.time()*1000),uuid.uuid4().hex)

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

Base = declarative_base()

class User(Base):
    __tablename__='users'
    id = Column(String(200),primary_key=True)
    email = Column(String(50))
    passwd = Column(String(50))
    admin = Column(SMALLINT())
    name = Column(String(50))
    image = Column(String(500))
    created_at = Column(TIMESTAMP())


engine = create_engine('mysql+mysqlconnector://data_op:data_op123@localhost:3306/aewsome')

DBSession = sessionmaker(bind=engine)

session = DBSession()

uid = next_id()
dtime = time.time()

new_user=User(id=uid,email='Ruanchenghua@hotmail.com',passwd='old',admin=1,name='Ruan',image='/image/0022.jpg',created_at=dtime)
session.add(new_user)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.name=='Ruan').one()
print('type:', type(id))
print('name:', user.name)
session.close()