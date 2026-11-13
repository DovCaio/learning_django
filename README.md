# Learning django

## Objective

Study the basic of django, using a crud of a perfume store.

sqlite3 is used to simplify

## How to execute

Install django in your pc, then execute:

```bash
python3 manage.py migrate
python3 manage.py runserver
```

The API is listen in 8000, and the began in /products

```
                                        and we have: /create   POST
                                                     /get_all  GET
                                                     /get_one  GET
                                                     /put      PUT
                                                     /delete   DELETE
```

The frontend of this was maked in flutter and is located in: https://github.com/DovCaio/learning_dart_and_flutter/tree/main/flutter/zefinha_perfumes_loja

## Differences about django

### Django give us a lot of ready to use things, we can have diferents entity features and this features are organizeds in differents directories, we start with:

```bash
python manage.py startapp ENTITY_NAME
```

and all the features gonna be inside of the ENTITY_NAME directory, like models and the view.

### We use settigs in the main project to configure the route base, dependecies and some ready to use middlewares

### The ORM of django let us change the migrations if we dont like what was done for him, so we use:

```bash
python manage.py makemigrations
```

to make the migration, and so the ENTITY_NAME/migrations directory gonna be fill with the new migrations that can be modifyed before this applications with:

```bash
python manage.py migrate
```
