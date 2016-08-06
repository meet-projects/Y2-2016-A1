from flask import Flask, render_template, url_for, request, redirect
from flask.sessions import SessionInterface, SessionMixin
from uuid import uuid4
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
#session["uid"]= uuid4()

#YOUR WEB APP CODE GOES HERE


india_info = ["President: Pranab Mukherjee (2012)","Prime Minister: Narendra Modi (2014)","Land area: 1,147,949 sq mi (2,973,190 sq km)", "total area: 1,269,338 sq mi (3,287,590 sq km)", "Population (2014 est.): 1,236,344,631 (growth rate: 1.25%)", "birth rate: 19.89/1000","infant mortality rate: 43.19/1000", "life expectancy: 67.8","Capital (2011 est.): New Delhi, 22.654 million","Largest cities: Mumbai 19.744 million; Kolkata 14.402 million; Chennai 8.784 million; Bangalore 8.614 million; Hyderabad 7.837 million (2011)", "Monetary unit: Rupee"]
france_info= ["President: Francois Hollande (2012)","Prime Minister: Manuel Valls (2014)","Land area: 210,688 squared miles (545,630 squared kilometres)","Total area: 211,209 squared miles(547,030 squared kilometres)","Population (2014 est.): 66,259,012  (growth rate:0,45%)","Birth rate: 12.49/1000","Infant mortality rate: 3.31/1000","Life expectancy: 81.66","Capital and largest city(2014 est.): Paris, 10.764 (metro. area)","Other large cities: Lyon, Marseille-Aix-en-Provence, Lille, Nice-Cannes,Toulouse."]
italy_info=["President: Sergio Mattarella (2015)","Prime Minister: Matteo Renzi (2014)","Land area: 113,521 sq mi (294,019 sq km); total area: 116,305 sq mi (301,230 sq km)","Population (2014 est.): 61,680,122 (growth rate: 0.3%); birth rate: 8.84/1000; infant mortality rate: 3.31/1000; life expectancy: 82.03","Capital and largest city (2011 est.): Rome, 3.298 million","ther large cities: Milan 2.909 million; Naples 2.373 million; Turin 1.613 million; Palermo 915,000; Bergamo 784,000 (2011)","Monetary unit: Euro (formerly lira)"]
usa_info=["President: Barack H. Obama (2009)","Vice President: Joseph Biden (2009)","Land area: 3,539,225 sq mi (9,166,601 sq km)"," total area: 3,718,691 sq mi (9,631,420 sq km)","Population (2014 est.): 318,892,103 (growth rate: 0.77%)", " birth rate: 13.42/1000", "infant mortality rate: 6.17/1000"," life expectancy: 79.56 ", "density per sq mi: 88.6","Capital (2013 est.): Washington, DC, 646,449","Largest cities (2013 est.): New York, 8,405,837; Los Angeles, 3,884,307; Chicago, 2,718,782; Houston, 2,195,914; Philadelphia, 1,553,165","Monetary unit: dollar","Languages: English 82.1%, Spanish 10.7%, other Indo-European 3.8%, Asian and Pacific island 2.7%, other 0.7% (2000)","Ethnicity/race (2010 Census): White: 223,553,265 (72.4%); Black: 38,929,319 (12.6%); Asian: 14,674,252 (4.8%); American Indian and Alaska Native: 2,369,431 (0.8%); Native Hawaiian and other Pacific Islander: 1,225,195 (0.4%); Hispanic origin:1 50,477,594 (16.3%)","Religions: Protestant 51.3%, Roman Catholic 23.9%, Mormon 1.7%, other Christian 1.6%, Jewish 1.7%, Buddhist 0.7%, Muslim 0.6%, other or unspecified 2.5%, unaffiliated 12.1%, none 4% (2007)"]
china_info= ["President: Xi Jinping (2013)","Prime Minister: Premier Li Keqiang (2013)","Land area: 3,600,927 sq mi (9,326,411 sq km); total area: 3,705,407 sq mi (9,596,960 sq km)1","Population (2014 est.): 1,355,692,576 (growth rate: 0.44%); birth rate: 12.17/1000; infant mortality rate: 14.79/1000; life expectancy: 75.15","Capital (2011 est.): Beijing, 15.594 million","Largest cities: Shanghai 20.208 million; Guangzhou 10.849 million; Shenzhen 10.63 million; Chongqing 9.977 million; Wuhan 9.158 million (2011)","Monetary unit: Yuan/Renminbi"]




@app.route("/")
def main():
    return render_template('main_page.html')

@app.route("/AboutUs")
def about_us():
    return render_template('about_us.html')

@app.route("/flag/<string:flag_name>/ cc ")
def flag(flag_name):
    title= flag_name
    quizzes= session.query(Quiz).filter_by(country=flag_name.capitalize()).all()
    picture= url_for('static', filename=flag_name+".png")
    return render_template('country.html',quizzes=quizzes, picture=picture , flag_name = flag_name.capitalize())
 

@app.route("/quiz/<string:country_name>/<int:quiz_id>/", methods= ["POST", "GET"])
def quiz(country_name,quiz_id ):
    if request.method=="GET":
        quiz= session.query(Quiz).filter_by(id=quiz_id).first()
        title= quiz.name
        quiz_question=session.query(Questions).filter_by(quiz_id=quiz_id).all()
        return render_template('quiz.html', country_name=country_name, quiz=quiz, title=title, quiz_question=quiz_question)
    else:
        score=0
        correct_questions = []
        incorrect_questions = []
        for question_id in request.form:
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
                print (correct_text == request.form[question_id])
                
                print ("USER ANSWER: ")
                if correct_text == request.form[question_id]:
                    print ("hello, correct matches user")
                    score=score+20;
                    correct_questions.append(request.form[question_id])
                else:
                    incorrect_questions.append(request.form[question_id])
        
        print (session['uid'])
                    
        return redirect (url_for('.result', country_name=country_name, score=score, quiz_id=quiz_id , incorrect_questions=incorrect_questions, correct_questions=correct_questions))

@app.route("/result/<string:country_name>/<int:quiz_id>/<int:score>")
def result(country_name,quiz_id, score ):
    incorrect_questions = session.args["incorrect_questions"]
    correct_questions= session.args["correct_questions"]
    print (correct_questions)
    questions=session.query(Questions).filter_by(quiz_id=quiz_id).all()
    quiz_ = session.query(Quiz).filter_by(id=quiz_id).first()
    quiz_name = quiz_.name
    question_to_answer = {}
    info = ''
    if country_name.capitalize() == 'India':
        info = india_info
    elif country_name == 'Usa':
        info = usa_info
    elif country_name== 'France':
        info=france_info
    elif country_name== 'China':
        info= china_info
    elif country_name== 'Italy':
        info= italy_info

    for question in questions:
        correct=question.correct
        if correct==1:
            correct_text=question.option_1
            question_to_answer[question.id]=correct_text

        elif correct==2:
            correct_text=question.option_2
            question_to_answer[question.id]=correct_text
        elif correct==3:
            correct_text=question.option_3
            question_to_answer[question.id]=correct_text
        else:
            correct_text=question.option_4
            question_to_answer[question.id]=correct_text

    return render_template('score.html', score=score, questions=questions, question_to_answer=question_to_answer, quiz_name=quiz_name, info=info, country_name=country_name, correct_questions=correct_questions )





if __name__ == '__main__':
    app.run(debug=True)
