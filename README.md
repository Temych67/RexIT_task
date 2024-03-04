# RexIT_task
 The data from the dataset will be loaded in the migration file after the model is created. 
 Also added a command that performs a similar process of adding data to the model.
The endpoint for obtaining customer category data is api/v1/clients/client_categories/. 
The endpoint for accessing swagger documentation api/v1/swagger/

##The project uses:
* [Python 3.10](https://www.python.org/downloads/release/python-3100/)
* [Django 5.0.3](https://www.djangoproject.com/download/)
* [Django REST framework 3.14](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/download/)

# Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).
## Basic Commands

### Setting Up Your Users

- To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

- To create a **client categories**, use this command:

        $ python manage.py add_client_categories

### Project

To launch a project using Docker compose, you need to follow these steps:

1. Clone a project from [GitHub](https://github.com/Temych67/RexIT_task).
2. Add the settings for the database (DATABASE_URL) to the .env file. For example,
```
DATABASE_URL="psql://user:password@host.docker.internal:port/db"
```
3. Execute the command `docker compose up --build`