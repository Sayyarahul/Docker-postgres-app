Docker + Python + PostgreSQL App

A beginner-friendly DevOps project that runs a Python application connected to a PostgreSQL database — fully containerized using Docker and Docker Compose.

This project helps you understand:

How Docker images and containers work

How to Dockerize a Python app

How to run PostgreSQL inside Docker

How to connect containers over a Docker network

How to use Docker Compose to manage multi-container apps

Project Structure
myproject/
│── app.py
│── Dockerfile
│── requirements.txt
│── docker-compose.yml
│── .dockerignore
└── README.md

Features

Python app waits for PostgreSQL to be ready

Creates a table in PostgreSQL

Inserts data

Reads and prints the inserted row

Fully isolated environment using Docker

Single command to run everything using Docker Compose

 1. Python Application (app.py)

This app:

Connects to PostgreSQL

Creates a table people

Inserts a row

Reads the row and prints it

2. Dockerfile (Python 3.13)

The Dockerfile:

Uses Python 3.13

Installs psycopg2 dependencies

Installs Python dependencies

Runs the application

3. Running the App With Docker Compose
▶ Start everything (App + Postgres)
docker-compose up --build

▶Run in background
docker-compose up -d --build

View logs
docker-compose logs -f app

Stop everything
docker-compose down

Stop and delete database volume
docker-compose down --volumes

4. Verify PostgreSQL Container
Check running containers
docker ps

Connect inside PostgreSQL container
docker exec -it my-postgres bash
psql -U user -d mydb


Inside PostgreSQL prompt:

SELECT * FROM people;


Exit:

\q
exit

5. Useful Docker Commands
Build image manually:
docker build -t my-python-app:3.13 .

Run Python app manually:
docker run --rm --network mynetwork my-python-app:3.13

Delete unused containers:
docker system prune -f

6. Git & GitHub Commands (For This Project)
Initialize Git:
git init

Add files:
git add .

Commit:
git commit -m "Initial commit"

Add GitHub remote:
git remote add origin https://github.com/Sayyarahul/Docker-postgres-apps.git

Push:
git push -u origin main

7. Environment Variables Used
Variable	Description
POSTGRES_USER	Username for DB
POSTGRES_PASSWORD	Password
POSTGRES_DB	Database name
POSTGRES_HOST	Hostname (container name)
POSTGRES_PORT	5432

These are automatically passed via docker-compose.yml.

8. Troubleshooting
 psycopg2 not installing?

Inside Dockerfile:

We already added all system dependencies: libpq-dev, build-essential, etc.

 App says “Postgres not ready”?

The app retries for 10 attempts (2 seconds each). Increase delay if needed.

 Git push fails?

Check remote:

git remote -v


Make sure it is:

https://github.com/Sayyarahul/Docker-postgres-apps.git

 9. What You Learned

Installing Docker

Running PostgreSQL inside Docker

Building Docker images

Connecting containers with networks

Using Docker Compose

Pushing a real project to GitHub

