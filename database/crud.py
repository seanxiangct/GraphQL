from models.models import Person, Address
from .config import SessionLocal

def get_persons() -> list[Person]:
    with SessionLocal() as session:
        persons = session.query(Person).filter(Person.addresses.any()).all()

        return persons

def add_person(name: str, email: str) -> Person:
    with SessionLocal() as session:
        person = Person(name=name, email=email)
        session.add(person)
        session.commit()
        return person