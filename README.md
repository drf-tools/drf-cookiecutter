# Django App Cookiecutter

This project helps to generate simple Django app.

## Features

* [See app README]({{cookiecutter.directory_name}}/README.md)

## Requirements

* [Cookiecutter](https://cookiecutter.readthedocs.io/)
	- A command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Django devops project:

```
cookiecutter https://github.com/drf-tools/drf-cookiecutter.git
```

## What's in it?



Here is the folder tree of generated source.
```
.
├── Dockerfile
├── README.md
├── bin
│   ├── banner.sh
│   ├── coverage-report.sh
│   ├── dj-build-dev.sh
│   ├── dj-build-prod.sh
│   ├── dj-initdata.sh
│   ├── dj-makemigrations.sh
│   ├── dj-migrate.sh
│   ├── dj-run.sh
│   ├── dj-test.sh
│   ├── dj.sh
│   ├── entrypoint.sh
│   └── install.sh
├── doc
│   ├── accounts
│   │   └── auth-apis.md
│   ├── environments.md
│   ├── index.md
│   └── security.md
├── docker-compose.test.yml
├── docker-compose.yml
├── requirements
│   ├── all.txt
│   ├── base.txt
│   ├── dev.txt
│   └── test.txt
└── src
    ├── accounts
    │   ├── __init__.py
    │   ├── apis.py
    │   ├── factories.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── permission.py
    │   ├── serializers.py
    │   └── tests
    │       ├── __init__.py
    │       └── test_apis_users.py
    ├── apis
    │   ├── __init__.py
    │   └── urls.py
    ├── app
    │   ├── __init__.py
    │   ├── constants.py
    │   ├── envs.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   ├── components
    │   │   │   ├── __init__.py
    │   │   │   ├── authentication.py
    │   │   │   ├── common.py
    │   │   │   ├── database.py
    │   │   │   └── logging.py
    │   │   └── environments
    │   │       ├── __init__.py
    │   │       ├── dev.py
    │   │       ├── local.py
    │   │       ├── prod.py
    │   │       ├── stag.py
    │   │       └── test.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── debugging
    │   ├── __init__.py
    │   ├── apps.py
    │   └── management
    │       └── commands
    │           ├── __init__.py
    │           └── initdata.py
    └── manage.py
```

## Configuration

### Required
-------------

* **directory_name**

    * Default: `app-api`

    * NOTE: **This should be as default for the other repos of the stack to work**

* **project_name**

    * You must give the your app name here. This should match with your `docker ID` as well.

    * So your images will have the format: `project_name/app-api:develop` for example.
