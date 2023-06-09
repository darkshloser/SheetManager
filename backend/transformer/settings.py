"""
Django settings for transformer project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8ew7hf41c8b__6r(p1*md@a-m=2%sq^)^an=awx7zr9saf4%)h'

# REST API settings
API_VERSION = 'api/v1/'
API_DOC_TITLE = 'API Documentation'
API_DOC_DESCRIPTION = 'Automatically generated API definitions'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'csvs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'transformer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.parent / 'frontend' / 'dist'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

WSGI_APPLICATION = 'transformer.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': []
}

# CORS permissions
CORS_ORIGIN_WHITELIST = 'http://localhost:8080',

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'HOST': DATABASE_HOST,
        'USER': DATABASE_USER,
        'PORT': '5432',
        'TEST': {
            'NAME': f'{DATABASE_NAME}_test',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
USE_TZ = True
TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.parent / 'frontend' / 'dist' / 'static'
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'backend')

# Bind mount for uploading *.csv files, which will not
# be removed once the backend container is down
CSV_DIR = "csv_files/"
CSV_PATH = os.path.join(MEDIA_ROOT, CSV_DIR)

# Celery
BROKER_URL = os.environ['BROKER_URL']
CELERY_BROKER_URL = f'{BROKER_URL}/0'
CELERY_RESULT_BACKEND = f'{BROKER_URL}/1'
CELERY_WORKER_CONCURRENCY = 1


# Caching with Redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f'{CELERY_RESULT_BACKEND}',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"
    }
}

# Cache individual csv documents for 30 minutes 
# and the entire list of all csv documents for 2 minutes.
CACHE_SINGLE_CSV_TTL = 60 * 30
CACHE_LIST_CSVS_TTL = 60 * 2

# Cache all the csv items under following 'key'
CACHE_ALL_CSVS_KEY = "722e1814-5832-4a82-90c5-59194226a811"
