#!/bin/bash

python backend/src/manage.py makemigrations
python backend/src/manage.py migrate
python backend/src/manage.py runserver 0:8000