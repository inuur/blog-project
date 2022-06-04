# Blog API on Django Rest Framework

## Docker compose
Before starting the app, create `.env.dev` file in the root of the project. File content for the development purposes:
```
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
```

To start app run `docker-compose up --build` in the root of the project

## Dummy test data

To generate dummy test data run command `python manage.py dummy_data`
It creates 50.000 users, make each user follow 100 blogs. Creates 200.000 post in random blogs. 