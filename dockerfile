# syntax=docker/dockerfile:1
FROM python:3.10

MAINTAINER Maxwell Mullin "inbox@max-was-here.com"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# ENTRYPOINT [ "python" ]

CMD [ "python" "app/main.py" ]