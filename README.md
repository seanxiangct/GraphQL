# GraphQL

GraphQL Endpoint: [/graphql](http://localhost:8000/graphql)

## To Run

Run the docker-compose.yml file to start up the service locally with the service and postgreSQL containers

To connect to the database:

1. shell into the database container
2. run `psql -U postgres graph_db`

To initialise database table, with all containers running, run:

`docker-compose exec graphql alembic upgrade head`

Go to the GraphQL endpoint and explore the API!

## To test

`docker-compose exec graphql pytest tests/`

## TODO

- [ ] fix testing
- [ ] add custom schema
- [ ] async db query
- [ ] exception handling and error message
- [ ] query all users under the same address
- [ ] pagination
- [ ] mutations
