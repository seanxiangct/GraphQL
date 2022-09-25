# GraphQL

GraphQL Endpoint: [/graphql](http://localhost:8000/graphql)

## To Run

Run the docker-compose.yml file to start up the services locally with the API service and postgreSQL containers

To connect to the database:

1. shell into the database container
2. run `psql -U postgres graph_db` connect to the service database

To initialise database table, with all containers running, run:

`docker-compose exec graphql alembic upgrade head`

Go to the GraphQL endpoint and explore the API!

> The current API supports query against **person only** with the following schema. The additional **edges** and **node** types are added for future cursor-based pagination and to reduce code duplication.

```graphql
query MyQuery {
  person {
    email
    name
    id
    addresses {
      edges {
        node {
          number
          street
          city
          state
        }
      }
    }
  }
}
```

## To test

`docker-compose exec graphql pytest tests/`

## TODO

- [x] many-to-many model
- [x] database migration
- [x] schema mapping
- [x] fix testing
- [ ] add custom schema
- [ ] async db query
- [ ] exception handling and error message
- [ ] query all users under the same address
- [ ] pagination
- [ ] mutations
