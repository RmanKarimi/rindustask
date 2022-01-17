# Rindus Task


### Features

1. create, read, update and delete users
2. authenticate using a Google account
3. Restrict manipulation operations on a user to the administrator who created them
4. Using PostgreSQL as the database backend
5. API documentation using Swagger
6. Using django-allauth


# Development

Following are instructions on setting up your development environment.

The recommended way for running the project locally and for development is using Docker.


## Docker Setup

This project is set up to run using [Docker Compose](https://docs.docker.com/compose/) by default. It is the recommended way. You can also use existing Docker Compose files as basis for custom deployment

1. Install Docker:
   - Linux - [get.docker.com](https://get.docker.com/)
   - Windows or MacOS - [Docker Desktop](https://www.docker.com/products/docker-desktop)
1. Clone this repo 

1. Start up the containers:

   ```sh
   $ docker-compose up
   ```
1. populate the Postgres DB (in a separate terminal):
   ```sh
   $ docker-compose exec web python3 manage.py makemigrations
   $ docker-compose exec web python3 manage.py migrate
   ```
1. Create a superuser if required:
   ```sh
   $ docker-compose exec web python3 manage.py createsuperuser
   ```

1. Users can login through this URL:
   
   ` http://localhost:8000/accounts/google/login/,`
