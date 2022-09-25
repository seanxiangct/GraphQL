import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Table, Enum, Identity
from sqlalchemy.orm import relationship

from database.config import Base

class StateEnum(enum.Enum):
    NSW = "NSW"
    VIC = "VIC"
    QLD = "QLD"
    SA = "SA"
    WA = "WA"
    TAS = "TAS"
    NT = "NT"
    ACT = "ACT"

association_table = Table(
    'association',
    Base.metadata,
    Column('person_id', Integer, ForeignKey('person.id'), primary_key=True),
    Column('address_id', Integer, ForeignKey('address.id'), primary_key=True)
)

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, Identity(), primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    addresses = relationship("Address", secondary=association_table, back_populates="persons")

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, Identity(), primary_key=True)
    number = Column(Integer)
    street = Column(String)
    city = Column(String)
    state = Column(Enum(StateEnum))
    persons = relationship("Person", secondary=association_table, back_populates="addresses")