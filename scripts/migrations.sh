#!/bin/bash

python3 developer_discover/manage.py db_connection
python3 developer_discover/manage.py makemigrations
python3 developer_discover/manage.py migrate

python3 developer_discover/manage.py runserver 0.0.0.0:8000
