#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    database = sys.argv[2]

    engine = create_engine(
        "mysql+mysqldb://{}@localhost/{}".format(username, database),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    stats_names = session.query(State).order_by(State.id).all()

    for _state in stats_names:
        print("{}: {}".format(_state.id, _state.name))

