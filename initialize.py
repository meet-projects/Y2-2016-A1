from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

<<<<<<< HEAD
from database_setup import Base, Quiz, Questions

engine = create_engine('sqlite:///project.db')

Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Quiz).delete()
session.query(Questions).delete()
session.commit()

# You can add some starter data for your database here.
