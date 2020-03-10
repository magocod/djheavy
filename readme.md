## Djheavy

* background tasks, django (celery)

## Framework

* Django -> https://www.djangoproject.com/

## Third Packages

* Celery -> https://docs.celeryproject.org/en/latest/index.html
* factory_boy -> https://factoryboy.readthedocs.io/en/latest/
* black -> https://black.readthedocs.io/en/stable/
* isort -> https://timothycrosley.github.io/isort/

## Tests (93% coverage)

* Python unittest -> https://docs.python.org/3/library/unittest.html
* Django tests -> https://docs.djangoproject.com/en/3.0/topics/testing/
* coverage -> https://coverage.readthedocs.io/en/coverage-5.0.3/

## instructions

Create a virtual python environment and install libraries with pip

```bash
pip install -r requirements.txt
```

Create all virtual environments (using tox)
```bash
tox
```

Migrate the database

```bash
python manage.py migrate
```

run tests (verify successful installation)
```bash
python manage.py test
```

run tests (verify coverage)
```bash
coverage run --source='.' manage.py test
coverage report
```

Run development server

```bash
python manage.py runserver
```

Enter the address

```bash
http://localhost:8000
```