import strawberry
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

from models.models import Person, Address

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()

# automatically generate strawberry types from sqlalchemy models
@strawberry_sqlalchemy_mapper.type(Person)
class Person:
    pass

@strawberry_sqlalchemy_mapper.type(Address)
class Address:
    pass

@strawberry.type
class Query:
    @strawberry.field
    def Person(self) -> Person:
        return Person(
            name="Patrick",
            email="test@email.com"
        )

# TODO: add mutation

strawberry_sqlalchemy_mapper.finalize()