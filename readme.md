Djheavy
=======
![Alt text](https://firebasestorage.googleapis.com/v0/b/django-237201.appspot.com/o/repo_tags%2Ftag_py_36_37.png?alt=media&token=54c1a277-f100-4e47-b5a7-09afe86c3550 "python_versions")
![Alt text](https://firebasestorage.googleapis.com/v0/b/django-237201.appspot.com/o/repo_tags%2Fcode_style_black.svg?alt=media&token=c4090132-fde3-4fb3-9e96-4e13d19bc1fb "code_style")

background task execution (django + celery)

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
pytest
```

run tests (verify coverage)
```bash
pytest --cov
```

Run development server

```bash
python manage.py runserver
```

Enter the address

```bash
http://localhost:8000
```
