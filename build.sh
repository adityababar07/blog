#!/bin/bash

python3 -m venv env

source env/bin/activate
# Install dependencies
pip3 install -r requirements.txt 

# Run database migrations
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput