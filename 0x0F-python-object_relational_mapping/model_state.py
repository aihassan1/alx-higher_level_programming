#!/usr/bin/python3
""" class definition of a State"""

from sqlalchemy import create_engine, Column, String, CHAR, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine(
    "mysql+mysqldb://root@localhost:3360/hbtn_0e_6_usa", echo=True)
Base = declarative_base()


class State(Base):
    """define the state class"""
    __tablename__ = "states"
    id = Column(
        "id", Integer, primary_key=True,
        autoincrement=True, nullable=False, unique=True
    )
    name = Column("name", CHAR(128), nullable=False)


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
session.close()
