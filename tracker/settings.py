"""
Django settings for tracker project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
from django.utils import crypto

# Make Cloud Foundry VCAP environment variables accessible
# https://github.com/jmcarp/py-cfenv
from cfenv import AppEnv
env = AppEnv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY = os.environ.get('SECRET_KEY',
                                         crypto.get_random_string(60))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True) != "False"

ALLOWED_HOSTS = ['*']


# Application definition

TEST_RUNNER = 'django_behave.runner.DjangoBehaveTestSuiteRunner'

INSTALLED_APPS = [
    'intake.apps.IntakeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'behave_django',
    'uaa_client',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'uaa_client.authentication.UaaBackend',
)

ROOT_URLCONF = 'tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASES = {
    'default': dj_database_url.config(
        default="postgres://postgres@db:5432/postgres"
        )
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# cloud.gov UAA Provider
# https://cg-django-uaa.readthedocs.io/

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

UAA_AUTH_URL = 'https://login.fr.cloud.gov/oauth/authorize'

UAA_TOKEN_URL = 'https://uaa.fr.cloud.gov/oauth/token'

uaa_service = env.get_service(name='tracker-uaa-creds')
if uaa_service is not None:
    UAA_CLIENT_ID = uaa_service.credentials['UAA_CLIENT_ID']

    UAA_CLIENT_SECRET = uaa_service.credentials['UAA_CLIENT_SECRET']
else:
    UAA_CLIENT_ID = os.environ.get('UAA_CLIENT_ID', 'tracker-dev')

    UAA_CLIENT_SECRET = os.environ.get('UAA_CLIENT_SECRET')

LOGIN_URL = 'uaa_client:login'

LOGIN_REDIRECT_URL = '/'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATICFILES_DIRS = []
