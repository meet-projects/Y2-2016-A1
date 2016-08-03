from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE


class Questions(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    question= Column(Integer)
    quiz_id= Column(Integer, ForeignKey('quiz.id'))
    option_1= Column(String)
    option_2= Column(String)
    option_3= Column(String)
    option_4= Column(String)
    Correct =Column(Integer)

class quiz(Base):
  __tablename__='quiz'
  id=Column(Integer, primary_key=True)
  country= Column(String)
  name=Column(String)

