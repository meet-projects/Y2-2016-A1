from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base

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

@app.route("/quiz/<string:flag_name>")
def flag(flag_name):
	if flag_name=="united states":
    	return render_template('united_states.html')
    elif flag_name=="china":
    	return render_template ("china.html")
    elif flag_name=="india":
    	return render_template("india.html")
    elif flag_name=="france":
    	return render_template("france.html")
    elif flag_name=="italy":
    	return render_template("italy.html")



if __name__ == '__main__':
    app.run(debug=True)
