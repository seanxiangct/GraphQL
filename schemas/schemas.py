import strawberry
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

import models.models as models
from database.crud import add_person, get_persons

@strawberry.type
class Address:
    id: int
    number: int
    street: str
    city: str
    state: models.StateEnum

    @classmethod
    def from_model(cls, model):
        return cls(
            id=model.id,
            number=model.number,
            street=model.street,
            city=model.city,
            state=model.state
        )

@strawberry.type
class Person:
    id: strawberry.ID
    name: str
    email: str
    address: list[Address]

    @classmethod
    def from_model(cls, model):
        return cls(
            id=model.id,
            name=model.name,
            email=model.email,
            address=[Address.from_model(address) for address in model.addresses]
        )

@strawberry.type
class Query:
    @strawberry.field
    def person(self) -> list[Person]:
        persons = get_persons()

        # convert models to strawberry types
        

        return [Person.from_model(person) for person in persons]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_person(self, name: str, email: str) -> Person:
        person = add_person(name, email)
        return person
