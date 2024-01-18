#!/usr/bin/python3
"""
Module for the class definition of a State.
"""


from sqlalchemy import create_engine, Column, Integer, VARCHAR
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine(
    "mysql+mysqldb://root@localhost:3360/hbtn_0e_6_usa", echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """Define the State class. and mention all the attr."""
    __tablename__ = "states"
    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )
    name = Column("name", VARCHAR(128), nullable=False)


# Create the table in the MySQL database
Base.metadata.create_all(bind=engine)


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Close the session after using it
session.close()
