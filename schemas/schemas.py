import enum

import strawberry
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

import models.models as models
from database.crud import add_person, get_persons

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()
@strawberry_sqlalchemy_mapper.type(models.Person)
class Person:
    pass
@strawberry_sqlalchemy_mapper.type(models.Address)
class Address:
    pass
@strawberry.type
class Query:
    @strawberry.field
    def person(self) -> list[Person]:
        persons = get_persons()
        return persons
            
        # return [Person.marshal(person) for person in persons]

@strawberry.type
class Mutation: 
    @strawberry.mutation
    def add_person(self, name: str, email: str) -> Person:
        person = add_person(name, email)
        return Person.marshal(person)

strawberry_sqlalchemy_mapper.finalize()