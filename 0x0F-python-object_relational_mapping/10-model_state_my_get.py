#!/usr/bin/python3
"""
a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_to_search = sys.argv[4]

    engine = create_engine(
        "mysql+mysqldb://{}@localhost/{}".format(username, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter_by(name=state_to_search).first()

    print("{}".format(result.id))

    session.close()
