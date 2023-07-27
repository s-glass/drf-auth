# Lab - Class 33
## Project: drf-auth

Author: Sarah Glass for Python 401
Collaborated with Anthony, Logan, Dan, Slava at a Remo table.

## Overview

- Let’s move our API closer to production grade by adding Authentication and switching to a Production Server

**Feature Tasks and Requirements - Django**

- Add JWT Authentication to your API.
- Install needed libraries in project configuration and/or site settings.
- Keep any pre-existing authentication so DRF Browsable API still usable.
- Install needed libraries in project configuration and/or site settings.


**Features - Docker**

- Switch to using Gunicorn instead of Django’s built in development server.
- mind the number of workers to avoid sluggishness
- Warning You will run into styling issues when you switch over to Gunicorn.
- On Django side you’ll need to properly handle static files using Whitenoise

**Storage Options**

- Your choice of SQLite or PostgreSQL
- Adjust docker-compose.yml so that data is persisted in a volume outside of container.
- These steps are different depending on whether SQLite or PostgreSQL is being used.


## Links and Resources

* TA and peer help.
* chatGPT helped with tests.

## Setup

- Gitignore includes venv.
- sample_env.txt includes env variables

## How to initialize/run your application

- python manage.py runserver
- docker compose up --build
- runs at `http://127.0.0.1:8000/api/v1/tacos`

## Libraries / Requirements

asgiref==3.7.2
Django==4.2.3
djangorestframework==3.14.0
psycopg2-binary==2.9.6
pytz==2023.3
sqlparse==0.4.4

## Tests

Built-in Django testing

- python manage.py test