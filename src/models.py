import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

coments_user= Table('coments_user', Base.metadata,
    Column('coments_id',ForeignKey('coments.id'), primary_key=True),
    Column('user_id',ForeignKey('user.id'), primary_key=True)
)

class User(Base):
    __tablename__='user'
    id= Column(Integer,primary_key= True)
    name = Column(String)
    user_name= Column(String)
    email= Column(String)
    post=relationship('post')
    coments= relationship('coments', secondary=coments_user)

class Post(Base):
    __tablename__='post'
    id=Column(Integer, primary_key=True)
    image=Column(String)
    title= Column(String)
    foot_photo=Column(String)
    id_user=Column(Integer, ForeignKey('user.id'))
    coments=relationship('Coments')


followers = Table('followers', Base.metadata,
    Column('id_user', ForeignKey('user.id'), primary_key=True),
    Column('id_follower', ForeignKey('user.id'), primary_key=True)
)

class Coments(Base):
    __tablename__='coments'
    id= Column(Integer, primary_key=True)
    coment=Column(String)
    id_post=Column(Integer,ForeignKey('post.id'))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e