# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Rick Ruan'

from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))
engine = create_engine('mysql+mysqlconnector://root:FonsView123@localhost:3306/test')

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user=User(id='3',name='BOB')
session.add(new_user)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id=='5' or User.id=='1').one()
print('type:', type(user))
print('name:', user.name)
session.close()
