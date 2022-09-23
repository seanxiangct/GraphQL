import email
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
class Person:
    email: str
    address: "Address"

@strawberry.type
class Address:
    number: int
    street: str
    city: str
    state: StateEnum


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> Person:
        return None

schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)


app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)