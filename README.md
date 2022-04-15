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

## Testing
Load tests can be found in the `testing_script/` folder. These can be run using [k6](https://k6.io/).

## Contributing

The bulk of the transaction server's functionality is written in the `transaction_server/transactions/` folder.
This is the location of the `transactions` Django app:

- `models.py` includes database schema information and business logic.
- `urls.py` includes a list of available views.
- `views.py` includes request handlers.
- `management/check_triggers.py` includes Celery logic.
- `../transaction_server/settings.py` includes initialization behaviour and application global constants.

Most other files are created by Django's command-line utility. Read up on [Django](https://docs.djangoproject.com/en/4.0/) before attempting to change them.

### Undesirable Design Artifacts
- `init.sql` is required to initialize a PostgreSQL without multiple restarts.
- The Django web service, Celery, and Celery Beat all use the same Docker image.
