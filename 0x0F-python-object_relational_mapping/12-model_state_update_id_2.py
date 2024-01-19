#!/usr/bin/python3
"""a script that changes the name of a State object
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}@localhost/{}".format(username, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    selected_state = session.query(State).filter_by(id=2).first()
    selected_state.name = "New Mexico"

    session.commit()
    session.close()
