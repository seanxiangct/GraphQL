from sqlalchemy.orm import joinedload

from models.models import Person, Address
from .config import SessionLocal

def get_persons() -> list[Person]:
    with SessionLocal() as session:

        # load all addresses for each person
        persons = session.query(Person)\
            .options(joinedload(Person.addresses)).all()

        return persons

def add_person(name: str, email: str) -> Person:
    with SessionLocal() as session:
        person = Person(name=name, email=email)
        session.add(person)
        session.commit()
        return person