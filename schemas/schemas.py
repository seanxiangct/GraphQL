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


# @strawberry.type
# class Address:
#     number: int
#     street: str
#     city: str
#     state: StateEnum

#     @classmethod
#     def marshal(cls, address: models.Address):
#         return cls(
#             number=address.number,
#             street=address.street,
#             city=address.city,
#             state=StateEnum[address.state],
#         )

# def get_addresses() -> list[Address]:
#     # TODO: get addresses from DB
#     return [
#         Address(number=1, street="Main Street", city="Sydney", state=StateEnum.NSW),
#         Address(number=2, street="Main Street", city="Sydney", state=StateEnum.NSW),
#     ]

# @strawberry.type
# class Person:
#     name: str
#     email: str
#     address: list[Address]
    
#     @classmethod
#     def marshal(cls, person: models.Person):
#         return cls(
#             name=str(models.Person.name),
#             email=str(models.Person.email),
#             address=[Address.marshal(address) for address in models.Person.addresses],
#         )

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