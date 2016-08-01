from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Questions 

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

id = Column(Integer, primary_key=True)
    question= Column(Integer)
    quiz.id= Column(Integer)
   	option_1= Column(String)
   	option_2= Column(String)
   	option_3= Column(String)
   	option_4= Column(String)
   	correct =Column(Boolean)

question_1= Questions(
	question="What is China's capital?",
	#quiz.id goes here
	option_1="Tokyo",
	option_2="Shanghai",
	option_3="Beijing",
	option_4="Hong Kong",
	Correct=3,
	)

session.commit()

