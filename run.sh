#!/usr/bin/env bash
export SECRET_KEY
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -U -r requirements.txt
python manage.py runserver