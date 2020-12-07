FROM python:3.8

WORKDIR code
COPY ./requirements.txt /code/

RUN apt-get update
RUN pip install -r /code/requirements

COPY . .

