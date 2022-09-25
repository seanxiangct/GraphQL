from models.models import Person, Address
from .config import SessionLocal

def get_persons() -> list[Person]:
    with SessionLocal() as session:
        return session.query(Person).all()

def add_person(name: str, email: str) -> Person:
    with SessionLocal() as session:
        person = Person(name=name, email=email)
        session.add(person)
        session.commit()
        return person

def get_addresses(person_id: str) -> list[Address]:
    with SessionLocal() as session:
        return session.query(Address).filter(Address.person_id == person_id).all()