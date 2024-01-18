#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa.
Contains State class and Base, an instance of declarative_base()
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State


username = sys.argv[1]
database = sys.argv[2]


engine = create_engine(
    "mysql+mysqldb://{}@localhost/{}".format(username, database),
    pool_pre_ping=True,
)

Session = sessionmaker(bind=engine)
session = Session()

stats_names = session.query(State).order_by(State.id).all()

for _state in stats_names:
    print("{}: {}".format(_state.id, _state.name))

session.close()
