# -*- coding: utf-8 -*-
"""
Django settings for development project.
settings/local

"""
from settings.base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'exampledb',
        'USER': 'example',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']
