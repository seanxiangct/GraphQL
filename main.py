from enum import Enum

import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

@strawberry.enum
class StateEnum(Enum):
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

def get_addresses(name: str) -> list[Address]:
    return [
        Address(number=1, street="Main Street", city="Sydney", state=StateEnum.NSW),
        Address(number=2, street="Main Street", city="Sydney", state=StateEnum.NSW),
    ]
    

@strawberry.type
class Person:
    name: str
    email: str
    # address: Address = strawberry.field(resolver=get_addresses(name))
    @strawberry.field
    def address(self) -> list[Address]:
        return get_addresses(self.name)

@strawberry.type
class Query:
    @strawberry.field
    def Person(self) -> Person:
        return Person(
            name="Patrick",
            email="test@email.com"
        )

schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)


app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)