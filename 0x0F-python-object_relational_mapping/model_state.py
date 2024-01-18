#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""

from sqlalchemy import create_engine, Column, Integer, VARCHAR, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine(
    "mysql+mysqldb://root@localhost:3360/hbtn_0e_6_usa", echo=True)

# Create a base class for declarative class definitions

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
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
