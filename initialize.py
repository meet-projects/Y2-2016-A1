from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


from database_setup import *

engine = create_engine('sqlite:///project.db')

Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

italy = Flag(flag_name = "italy" , flag_source = "Italy.png")
france= Flag(flag_name = "france" , flag_source = "France.png") 
india = Flag(flag_name = "india" , flag_source = "India.png")
china = Flag(flag_name = "china" , flag_source = "China.png")
usa   = Flag(flag_name = "usa" , flag_source = "Usa.png")
argentina =Flag(flag_name ="argentina" , flag_source= "Argentina.png")

session.add(argentina)
session.add(italy)
session.add(france)
session.add(india)
session.add(china)
session.add(usa)
session.commit()

# You can add some starter data for your database here.
   