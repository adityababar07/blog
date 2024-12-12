#!/bin/bash

python3.9 -m pip3 install --upgrade pip
python3.9 -m pip3 install pipenv
python3.9 -m pipenv shell
# Install dependencies
pip3 install -r requirements.txt 

# Run database migrations
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput