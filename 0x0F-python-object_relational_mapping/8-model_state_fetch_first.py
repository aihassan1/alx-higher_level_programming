#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}@localhost/{}".format(username, database),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_1 = session.query(State).order_by(State.id).first()
    if state_1:
        print("{}: {}".format(state_1.id, state_1.name))
    else:
        print("Nothing")

    session.close()
