import enum

import strawberry
# from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

import models.models as models
from database.crud import add_person, get_addresses, get_persons

# strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()

# automatically generate strawberry types from sqlalchemy models
# @strawberry_sqlalchemy_mapper.type(StateEnum)
# class StateEnum:
#     pass

# @strawberry_sqlalchemy_mapper.type(Person)
# class Person:
#     pass

# @strawberry_sqlalchemy_mapper.type(Address)
# class Address:
#     pass

@strawberry.enum
class StateEnum(enum.Enum):
    NSW = "NSW"
    VIC = "VIC"
    QLD = "QLD"
    SA = "SA"
    WA = "WA"
    TAS = "TAS"
    NT = "NT"
    ACT = "ACT"

@strawberry.type
class Address:
    number: int
    street: str
    city: str
    state: StateEnum

    @classmethod
    def marshal(cls, address: models.Address):
        return cls(
            number=address.number,
            street=address.street,
            city=address.city,
            state=StateEnum[address.state],
        )

# def get_addresses(name: str) -> list[Address]:
#     # TODO: get addresses from DB
#     return [
#         Address(number=1, street="Main Street", city="Sydney", state=StateEnum.NSW),
#         Address(number=2, street="Main Street", city="Sydney", state=StateEnum.NSW),
#     ]

@strawberry.type
class Person:
    name: str
    email: str
    address: list[Address]
    # @strawberry.field
    # def address(self) -> list[Address]:
    #     return get_addresses(self.id)
    
    @classmethod
    def marshal(cls, person: models.Person):
        return cls(
            name=str(models.Person.name),
            email=str(models.Person.email),
            address=[Address.marshal(address) for address in models.Person.addresses],
        )


@strawberry.type
class Query:
    @strawberry.field
    def person(self) -> list[Person]:
        persons = get_persons()
        return [Person.marshal(person) for person in persons]

@strawberry.type
class Mutation: 
    @strawberry.mutation
    def add_person(self, name: str, email: str) -> Person:
        person = add_person(name, email)
        return Person.marshal(person)

# strawberry_sqlalchemy_mapper.finalize()