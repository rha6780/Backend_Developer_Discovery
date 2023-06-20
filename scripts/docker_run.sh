#!/bin/bash

sudo python3 developer_discover/manage.py db_connection
sudo python3 developer_discover/manage.py makemigrations
sudo python3 developer_discover/manage.py migrate

sudo python3 developer_discover/manage.py runserver 0:80
