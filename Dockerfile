# FROM ubuntu:18.04
# FROM python:3.10-slim

# RUN apt-get -y update && apt-get -y dist-upgrade

# # apt-utils dialog : 우분투 초기 설정 / libpq-dev : PostgreSQL 의존성
# RUN apt-get install -y apt-utils dialog libpq-dev

# WORKDIR /webapp

# ### python 설치 ###
# ENV PYTHONUNBUFFERED=1

# ENV PYTHONIOENCODING=utf-8

# COPY Pipfile* ./

# ### 실행 환경 구축 ###
# RUN pip install --upgrade pip && pip install pipenv && pipenv install --system --dev --ignore-pipfile

# # RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

# COPY . ./

FROM python:3.10.0-slim

# set working directory
WORKDIR .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install project dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN chmod +x /requirements.txt
RUN pip install -r /requirements.txt

# add app
COPY . ./

# port open
EXPOSE 8000