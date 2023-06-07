FROM ubuntu:18.04 as base
FROM python:3.10.0-slim

# set working directory 
WORKDIR .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install project dependencies
## apt-utils dialog : 우분투 초기 설정 / libpq-dev : PostgreSQL 의존성
RUN apt update -y && apt install -y build-essential libpq-dev

## pip 라이브러리 설치
RUN pip install --upgrade pip
RUN pip install psycopg2-binary --no-binary psycopg2-binary

COPY ./requirements.txt /requirements.txt

RUN chmod +x /requirements.txt
RUN pip install -r /requirements.txt

# add app
COPY . ./

# port open
EXPOSE 8000