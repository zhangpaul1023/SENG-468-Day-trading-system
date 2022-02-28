# syntax=docker/dockerfile:1

# This file was taken from Docker's sample applications documentation. See:
# https://docs.docker.com/samples/django/

FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
