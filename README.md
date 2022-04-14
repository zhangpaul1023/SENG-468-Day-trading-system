# SENG468 Project

Course project for SENG468 - Software System Scalability at the University of Victoria

## Setup

From the project's root directory

    $ cd transaction_server

Build the project. Redo this if there are issues related to celery

    $ docker-compose build

To get the database setup, or if you make changes to the models

    $ docker-compose run web0 python3 manage.py makemigrations
    $ docker-compose run web0 python3 manage.py migrate

    $ docker-compose run web1 python3 manage.py makemigrations
    $ docker-compose run web1 python3 manage.py migrate

    $ docker-compose run web2 python3 manage.py makemigrations
    $ docker-compose run web2 python3 manage.py migrate

If you ever want to erase the database

    $ docker-compose run web0 python3 manage.py flush
    $ docker-compose run web0 python3 manage.py flush
    $ docker-compose run web0 python3 manage.py flush

Alternatively,

    $ rm -rf db

After building the project and setting up the database, you can run the application

    $ docker-compose up

You can tear the application down

    $ docker-compose down



