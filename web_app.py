from flask import Flask, render_template, url_for
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base, Quiz

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
	
	quizzes= session.query(Quiz).filter_by(country=flag_name.capitalize()).all()
	picture= url_for('static', filename=flag_name+".png")
	return render_template('country.html',quizzes=quizzes, picture=picture , flag_name = flag_name.capitalize())
 

@app.route("/quiz/<int:quiz_id>/")
def quiz(quiz_id):
	quiz= session.query(Quiz).filter_by(id=quiz_id).first()
	title= quiz.name+str(quiz.num)
	return render_template('quiz.html', quiz=quiz, title=title )





if __name__ == '__main__':
	app.run(debug=True)
