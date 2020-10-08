"""
Django settings for djheavy project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import json
import os

import dj_database_url

# heroku
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = None

with open(os.path.join(BASE_DIR, "django.config.json")) as json_file:
    ENV = json.load(json_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# Heroku hosting
ACTIVE_HEROKU = ENV["ACTIVE_HEROKU"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV["DEBUG"]

ALLOWED_HOSTS = ENV["ALLOWED_HOSTS"]


# Application definition

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party
    "corsheaders",
    "rest_framework",
    "django_celery_results",
    # local Django
    "apps.dbcache",
    "apps.mail"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "djheavy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djheavy.wsgi.application"

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = ENV["CORS_ORIGIN_WHITELIST"]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "Access-Control-Allow-Origin",
)

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination." + "PageNumberPagination",
    "PAGE_SIZE": 2,
    "DEFAULT_METADATA_CLASS": "rest_framework.metadata.SimpleMetadata",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        # "TEST": {
        #     "NAME": os.path.join(BASE_DIR, "test_db.sqlite3")
        # },
    },
    # "default": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "djheavy",
    #     "USER": "root",
    #     "PASSWORD": "",
    #     "HOST": "127.0.0.1",
    #     "PORT": 3306,
    # },
}

# CELERY CONFIG

CELERY_ACTIVATE = ENV["CELERY"]["ACTIVATE"]
CELERY_BROKER_URL = ENV["CELERY"]["CELERY_BROKER_URL"]
CELERY_RESULT_BACKEND = ENV["CELERY"]["CELERY_RESULT_BACKEND"]
CELERY_ACCEPT_CONTENT = ENV["CELERY"]["CELERY_ACCEPT_CONTENT"]
CELERY_TASK_SERIALIZER = ENV["CELERY"]["CELERY_TASK_SERIALIZER"]
CELERY_RESULT_SERIALIZER = ENV["CELERY"]["CELERY_RESULT_SERIALIZER"]

CELERY_CACHE_BACKEND = "default"

# CACHE
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django-cache",
    }
}

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 30

# EMAIL
ACTIVE_EMAIL = ENV["EMAIL"]["ACTIVE_EMAIL"]

EMAIL_BACKEND = ENV["EMAIL"]["EMAIL_BACKEND"]
EMAIL_HOST = ENV["EMAIL"]["EMAIL_HOST"]
EMAIL_USE_TLS = ENV["EMAIL"]["EMAIL_USE_TLS"]
EMAIL_PORT = ENV["EMAIL"]["EMAIL_PORT"]
EMAIL_HOST_USER = ENV["EMAIL"]["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = ENV["EMAIL"]["EMAIL_HOST_PASSWORD"]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        + "UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

IS_CI = os.environ.get("IS_CI", False)
if not IS_CI and ACTIVE_HEROKU:  # pragma: no cover
    django_heroku.settings(locals())
    if not DEBUG:
        DATABASES["default"] = dj_database_url.config(
            conn_max_age=600, ssl_require=True
        )
