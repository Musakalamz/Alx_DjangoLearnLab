# LibraryProject — Introduction to Django

This project initializes a clean Django setup to explore core concepts: project structure, configuration, and running the development server.

## Prerequisites
- Python 3.12+
- Django installed in your environment

Verify Django:

```bash
python -c "import django; print(django.get_version())"
```

## Getting Started
Run the development server from the project root:

```bash
python manage.py runserver
```

Visit the default Django welcome page:
- http://127.0.0.1:8000/

## Project Structure Overview
- [manage.py](file:///c:/Users/USER/OneDrive/Desktop/Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject/manage.py): Entry point for Django commands.
- [settings.py](file:///c:/Users/USER/OneDrive/Desktop/Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject/LibraryProject/settings.py): Project configuration (apps, middleware, templates, database).
- [urls.py](file:///c:/Users/USER/OneDrive/Desktop/Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject/LibraryProject/urls.py): URL routing “table of contents” for the site.
- [wsgi.py](file:///c:/Users/USER/OneDrive/Desktop/Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject/LibraryProject/wsgi.py): WSGI entry point for production servers.
- [asgi.py](file:///c:/Users/USER/OneDrive/Desktop/Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject/LibraryProject/asgi.py): ASGI entry point for async servers.

Database (SQLite by default):
- [db.sqlite3](file:///c:/Users/USER/OneDrive/Desktop/Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject/db.sqlite3)

## Common Commands
- Start server: `python manage.py runserver`
- Make migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Open shell: `python manage.py shell`

## Next Steps
- Create a Django app for domain models.
- Define models and perform CRUD using the Django shell.
- Register models in the Django admin and customize admin views.

