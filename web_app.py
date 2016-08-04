from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE


@app.route('/')
def main():
	return render_template('main_page.html')

@app.route("/flag/<string:flag_name>/")
def flag(flag_name):
	title= flag_name
	quizzes= session.query(Quiz).filter_by(country=flag_name.capitalize()).all()
	picture= url_for('static', filename=flag_name+".png")
	return render_template('country.html',quizzes=quizzes, picture=picture , flag_name = flag_name.capitalize())
 

@app.route("/quiz/<int:quiz_id>/", methods= ["POST", "GET"])
def quiz(quiz_id ):
	if request.method=="GET":
		quiz= session.query(Quiz).filter_by(id=quiz_id).first()
		title= quiz.name
		quiz_question=session.query(Questions).filter_by(quiz_id=quiz_id).all()
		return render_template('quiz.html', quiz=quiz, title=title, quiz_question=quiz_question)
	else:
		for question_id in request.form:
			
			score=0
			if question_id!= "submit":
				
				question=session.query(Questions).filter_by(id=int(question_id)).first ()
				correct=question.correct
				
				if correct==1:
					correct_text=question.option_1
				elif correct==2:
					correct_text=question.option_2
				elif correct==3:
					correct_text=question.option_3
				else:
					correct_text=question.option_4

				print("CORRECT: ", correct_text)
				print("user: ", request.form[question_id])
				print correct_text == request.form[question_id]
				

				print ("USER ANSWER: ")
				if correct_text == request.form[question_id]:
					print ("hello, correct matches user")
					score=score+20;
					
		return redirect (url_for('result', score=score, quiz_id=quiz_id))

@app.route("/result/<int:quiz_id>/<int:score>")
def result(quiz_id, score):
	questions=session.query(Questions).filter_by(quiz_id=quiz_id).all()
	question_to_answer = {}

	for question in questions:
		correct=question.correct
		if correct==1:
			correct_text=question.option_1
		elif correct==2:
			correct_text=question.option_2
		elif correct==3:
			correct_text=question.option_3
		else:
			correct_text=question.option_4
	question_to_answer[question.id]=correct_text

	return render_template('score.html', score=score, questions=questions, question_to_answer=question_to_answer)





if __name__ == '__main__':
	app.run(debug=True)
