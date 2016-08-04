from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class quiz(Base):
  __tablename__='quiz'
  id=Column(Integer, primary_key=True)
  country= Column(String)
  name=Column(String)

class Answers(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    question= Column(Integer)
    quiz_id= Column(Integer)
    option_1= Column(String)
    option_2= Column(String)
    option_3= Column(String)
    option_4= Column(String)
    correct =Column(Boolean)


