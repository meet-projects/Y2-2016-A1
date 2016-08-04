from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Questions, Quiz

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


china_quiz_1=Quiz(
	country="China",
	name="China 1"
	)
china_quiz_2=Quiz(
   country="China",
   name="China 2"
)
france_quiz_1=Quiz(
 country="France",
 name="France 1"
)
france_quiz_2=Quiz(
	country="France",
	name="France 2"
)
usa_quiz_1=Quiz(
  country="Usa",
  name="United States 1"
)
usa_quiz_2=Quiz(
  country="Usa",
  name="United States 2"
)
india_quiz_1=Quiz(
	country="India",
	name="India 1"
)
india_quiz_2=Quiz(
	country="India",
	name="India 2"
)


session.add(china_quiz_1)
session.add(china_quiz_2)
session.add(france_quiz_1)
session.add(france_quiz_2)
session.add(usa_quiz_1)
session.add(usa_quiz_2)
session.add(india_quiz_1)
session.add(india_quiz_2)
session.commit()

china_1_question_1= Questions(
#quiz 1
	quiz_id=china_quiz_1.id,
	question="What is China's capital?",
	option_1="Tokyo",
	option_2="Shanghai",
	option_3="Beijing",
	option_4="Hong Kong",
	correct=3
	)
china_1_question_2=Questions(
 quiz_id=china_quiz_1.id,
 question="What is the population of China?",
 option_1="1.3 billion",
 option_2="1.5 billion",
 option_3="1 billion",
 option_4="2 billion",
 correct=1
 )
china_1_question_3=Questions(
quiz_id=china_quiz_1.id,
question="What is the currency in China?",
option_1="Dollars",
option_2="Euro",
option_3="Renmibi",
option_4="Pounds",
correct=3
)
china_1_question_4=Questions(
quiz_id=china_quiz_1.id,
question="What is a traditional Chinese food?",
option_1="Ma Po tofu",
option_2="Wontons",
option_3="Dumplings",
option_4="Noodles",
correct=3
)
china_1_question_5=Questions(
quiz_id=china_quiz_1.id,
question="What percent of Chinese people are religious?",
option_1="7%",
option_2="5%",
option_3="15%",
option_4="10%",
correct=1
)

#quiz 2 - China:
china_2_question_1=Questions(
quiz_id=china_quiz_2.id,
question="What is China's dialing code?",
option_1="+972",
option_2="+1",
option_3="+61",
option_4="+86",
correct=4
)
china_2_question_2=Questions(
quiz_id=china_quiz_2.id,
question="How many rivers are there in China?",
option_1="22,000",
option_2="50,000",
option_3="45,000",
option_4="40,000",
correct=2
)
china_2_question_3=Questions(
quiz_id=china_quiz_2.id,
question="How many people live on less than 1 dollar per day?",
option_1="100 million",
option_2="50 million",
option_3="150 million",
option_4="200 million",
correct=1
)
china_2_question_4=Questions(
quiz_id=china_quiz_2.id,
question="When was the first paper money created in China?",
option_1="1,000 years ago",
option_2="1,300 years ago",
option_3="1,400 years ago",
option_4="500 years ago",
correct=3
)
china_2_question_5=Questions(
quiz_id=china_quiz_2.id,
question="A new skyscraper is built in china every ______",
option_1="5 minutes",
option_2="5 days",
option_3="5 years",
option_4="5 weeks",
correct=2
)

#France quiz 1

france_1_question_1= Questions(
	quiz_id=france_quiz_1.id,
	question="What is the capital of France?",
	option_1="Paris",
	option_2="New York",
	option_3="Tokyo",
	option_4="London",
	correct=1
)
france_1_question_2= Questions(
	quiz_id=france_quiz_1.id,
	question="What is the currency in France?",
	option_1="Dollars",
	option_2="Euro",
	option_3="Shekel",
	option_4="Dinar",
	correct=2
)
france_1_question_3= Questions(
	quiz_id=france_quiz_1.id,
	question="Who's France's president?",
	option_1="Pranab Mukherjee",
	option_2="Sergio Mattarella",
	option_3="Francois Holland",
	option_4="Barack Obama",
	correct=3
)
france_1_question_4= Questions(
	quiz_id=france_quiz_1.id,
	question="What are the colours in the French flag?",
	option_1="Red, Green, White",
	option_2="Green, White, Red",
	option_3="Blue & White",
	option_4="Blue, White, Red",
	correct=4
)
france_1_question_5= Questions(
	quiz_id=france_quiz_1.id,
	question="France once controlled more than _____ of the world's land",
	option_1="10%",
	option_2="5%",
	option_3="8%",
	option_4="2%",
	correct=3
)
france_2_question_1= Questions(
	quiz_id=france_quiz_2.id,
	question="France uses _____ different time zones",
	option_1="10",
	option_2="12",
	option_3="5",
	option_4="8",
	correct=2
)
france_2_question_2= Questions(
	quiz_id=france_quiz_2.id,
	question="What is France's population?",
	option_1="66 million",
	option_2="60 million",
	option_3="10 million",
	option_4="70 million",
	correct=1
)
france_2_question_3= Questions(
	quiz_id=france_quiz_2.id,
	question="What from the following is common bread in France?",
	option_1="White bread",
	option_2="fougasse",
	option_3="Pane Casareccio",
	option_4="Adobe bread",
	correct=2
)
france_2_question_4= Questions(
	quiz_id=france_quiz_2.id,
	question="Louis XIX was king of France for just _____",
	option_1="2 days",
	option_2="20 minutes",
	option_3="One day",
	option_4="One year",
	correct=2
)
france_2_question_5= Questions(
	quiz_id=france_quiz_2.id,
	question="When was the French revolution?",
	option_1="1850-1900",
	option_2="2000-2010",
	option_3="1789-1799",
	option_4="1650-1720",
	correct=3
)
usa_1_question_1= Questions(
	quiz_id=usa_quiz_1.id,
	question="When is the US independance day?",
	option_1="15th of October, 1988",
	option_2="4th of July, 1776",
	option_3="16th of January, 1770",
	option_4="6th of December, 1890",
	correct=2
)
usa_1_question_2= Questions(
	quiz_id=usa_quiz_1.id,
	question="Who was the US's third president?",
	option_1="Abraham Lincoln",
	option_2="George Washington",
	option_3="Donald Trump",
	option_4="Thomas Jefferson",
	correct=4
)
usa_1_question_3= Questions(
	quiz_id=usa_quiz_1.id,
	question="Which one of the following is an American national holiday?",
	option_1="Thanksgiving Day",
	option_2="Dragon Boat festival",
	option_3="Whit monday",
	option_4="Ascension Thursday",
	correct=1
)
usa_1_question_4= Questions(
	quiz_id=usa_quiz_1.id,
	question="What is the US's capital?",
	option_1="California",
	option_2="Washington DC",
	option_3="Washington",
	option_4="New York",
	correct=2
)
usa_1_question_5= Questions(
	quiz_id=usa_quiz_1.id,
	question="What is the US's population?",
	option_1="1.2 billion",
	option_2="23 million",
	option_3="35 million",
	option_4="318 million",
	correct=4
)
usa_2_question_1= Questions(
	quiz_id=usa_quiz_2.id,
	question="What is the supreme law of the land?",
	option_1="Independance",
	option_2="American",
	option_3="Oslo",
	option_4="Constitution",
	correct=4
)
usa_2_question_2= Questions(
	quiz_id=usa_quiz_2.id,
	question="How many states are in the US?",
	option_1="60",
	option_2="49",
	option_3="50",
	option_4="14",
	correct=3
)
usa_2_question_3= Questions(
	quiz_id=usa_quiz_2.id,
	question="Which president freed slaves?",
	option_1="Abraham Lincoln",
	option_2="George Washington",
	option_3="Taha Khalaf",
	option_4="Bill Clinton",
	correct=1
)
usa_2_question_4= Questions(
	quiz_id=usa_quiz_2.id,
	question="Where is the White House located?",
	option_1="New York",
	option_2="Boston",
	option_3="Chicago",
	option_4="Washington DC",
	correct=4
)
usa_2_question_5= Questions(
	quiz_id=usa_quiz_2.id,
	question="Which president was the only one to serve more than two terms?",
	option_1="George Washington",
	option_2="Woodrow Wilson",
	option_3="Franklin D Rosevelt",
	option_4="James Madison",
	correct=3
)
india_1_question_1=Questions(
	quiz_id=india_quiz_1.id,
	question="What is the traditional clothing in India?",
	option_1="bracce",
	option_2="sari",
	option_3="lace",
	option_4="ombaz",
	correct=2
	)
india_1_question_2=Questions(
	quiz_id=india_quiz_1.id,
	question="Where is India?",
	option_1="West Europe",
	option_2="North Africa",
	option_3="South Asia",
	option_4="North America",
	correct=3
	)
india_1_question_3=Questions(
	quiz_id=india_quiz_1.id,
	question="How many people live in India?",
	option_1="1.5 billion people",
	option_2="1.2 billion people",
	option_3="500 million people",
	option_4="90 million people",
	correct=2
	)
india_1_question_4=Questions(
	quiz_id=india_quiz_1.id,
	question="What is a traditional food in India?",
	option_1="Pasta",
	option_2="Shawarma",
	option_3="Pumpkin soup",
	option_4="Biryani",
	correct=4
	)
india_1_question_5=Questions(
	quiz_id=india_quiz_1.id,
	question="How many states are there in India?",
	option_1="1",
	option_2="29",
	option_3="35",
	option_4="55",
	correct=2
	)
india_2_question_1=Questions(
	quiz_id=india_quiz_2.id,
	question="What is the common Indian religion?",
	option_1="Islam",
	option_2="Jewdaism",
	option_3="Christianity",
	option_4="Hinduism",
	correct=4
	)
india_2_question_2=Questions(
	quiz_id=india_quiz_2.id,
	question="Who is the president of India?",
	option_1="Xi Jinping",
	option_2="Jacob Zuma",
	option_3="Robert Mugabe",
	option_4="Pranab Mukherjee",
	correct=4
	)
india_2_question_3=Questions(
	quiz_id=india_quiz_2.id,
	question="What is the common language in India?",
	option_1="Indo-Aryan languages",
	option_2="Dravidian languages",
	option_3="Austroasiatic",
	option_4="Sino-Tibetan",
	correct=1
	)
india_2_question_4=Questions(
	quiz_id=india_quiz_2.id,
	question="Who discovered India?",
	option_1="Colombus",
	option_2="Vasco de Gama",
	option_3="Silva Neto",
	option_4="Kransisko",
	correct=2
	)
india_2_question_5=Questions(
	quiz_id=india_quiz_2.id,
	question="When did India become independant?",
	option_1="1950",
	option_2="1947",
	option_3="1934",
	option_4="1889",
	correct=2
	)
session.add(china_1_question_1)
session.add(china_1_question_2)
session.add(china_1_question_3)
session.add(china_1_question_4)
session.add(china_1_question_5)
session.add(china_2_question_1)
session.add(china_2_question_2)
session.add(china_2_question_3)
session.add(china_2_question_4)
session.add(china_2_question_5)
session.add(france_1_question_1)
session.add(france_1_question_2)
session.add(france_1_question_3)
session.add(france_1_question_4)
session.add(france_1_question_5)
session.add(france_2_question_1)
session.add(france_2_question_2)
session.add(france_2_question_3)
session.add(france_2_question_4)
session.add(france_2_question_5)
session.add(usa_1_question_1)
session.add(usa_1_question_2)
session.add(usa_1_question_3)
session.add(usa_1_question_4)
session.add(usa_1_question_5)
session.add(usa_2_question_1)
session.add(usa_2_question_2)
session.add(usa_2_question_3)
session.add(usa_2_question_4)
session.add(usa_2_question_5)
session.add(india_1_question_1)
session.add(india_1_question_2)
session.add(india_1_question_3)
session.add(india_1_question_4)
session.add(india_1_question_5)
session.add(india_2_question_1)
session.add(india_2_question_2)
session.add(india_2_question_3)
session.add(india_2_question_4)
session.add(india_2_question_5)

session.commit()

