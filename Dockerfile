FROM ubuntu:18.04

RUN apt-get -y update && apt-get -y dist-upgrade

# apt-utils dialog : 우분투 초기 설정 / libpq-dev : PostgreSQL 의존성
RUN apt-get install -y apt-utils dialog libpq-dev


### python 설치 ###
COPY Pipfile Pipfile.lock ./
RUN apt-get install -y python3-pip python3-dev

ENV PYTHONUNBUFFERED=0

ENV PYTHONIOENCODING=utf-8

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

### 실행 환경 구축 ###
RUN pip3 install pipenv && pipenv install --dev --system --deploy

# RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

### 작업 디렉토리 ###
RUN mkdir /studyrun;

WORKDIR /studyrun