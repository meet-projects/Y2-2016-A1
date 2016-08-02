from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Questions 

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


quiz_1=quiz(
	country="China"
	name="China_1"

	)
info_quiz_1=session.query(quiz).filter_by(id=question_1.quiz_id).one()
info_quiz_1.country
session.add(quiz_1)
session.commit()
question_1= Questions(
#quiz 1
	quiz_id=quiz_1.id,
	question="What is China's capital?",
	option_1="Tokyo",
	option_2="Shanghai",
	option_3="Beijing",
	option_4="Hong Kong",
	Correct=3,
	)

session.commit()

