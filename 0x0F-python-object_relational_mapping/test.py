from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, CHAR, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "People"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String(length=50))
    lastname = Column("lastname", String(length=50))
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return "{} {} {} {} {}".format(
            self.ssn, self.firstname, self.lastname, self.gender, self.age
        )


class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", Text)
    owner = Column("owner", Integer, ForeignKey("People.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return "{} {} {}".format(self.tid, self.description, self.owner)


engine = create_engine("mysql://root@localhost:3306/testing", echo=True)


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(124544, "Mike", "smith", "M", 32)
session.add(person)
session.commit()

people_to_add = [
    Person(121424, "Aron", "call", "M", 40),
    Person(133344, "zak", "sold", "M", 36),
    Person(555574, "jack", "shad", "M", 92),
]

session.add_all(people_to_add)
session.commit()

t1 = Thing(1, "box", person.ssn)
session.add(t1)
session.commit()


person_to_assign = session.query(Person).filter_by(ssn=121424).first()

t2 = Thing(2, "car", person_to_assign.ssn)

session.add(t2)
session.commit()
