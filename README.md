# User GraphQL

GraphQL Endpoint: /graphql[http://localhost:8000/graphql]

## To Run

Run the docker-compose.yml file to start up the service locally with the service and postgreSQL containers

To connect to the database:

1. shell into the database container
2. run `psql -U postgres graph_db`

To initialise database table, with all containers running, run:

`docker-compose exec graphql alembic upgrade head`
