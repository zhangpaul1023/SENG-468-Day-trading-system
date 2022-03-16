# SENG468 Project

Course project for SENG468 - Software System Scalability at the University of Victoria

## Setup Workload Test
To start server process:
```sh
cd transaction_server
sudo rm -r data/db/
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py loaddata fixtures/workload.yaml
docker-compose up
```
To launch test from terminal client:
```sh
cd cli
./client.py ./workload.txt http://localhost:8000/transactions/workload
```
