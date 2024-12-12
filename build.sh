#!/bin/bash

python3.9 -m pip install --upgrade pip
python3.9 -m pip install pipenv
python3.9 -m pipenv shell
# Install dependencies
pip install -r requirements.txt 

# Run database migrations
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput