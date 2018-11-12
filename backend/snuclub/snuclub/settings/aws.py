from django.core.exceptions import ImproperlyConfigured

from .loader import load_credential
from .base import *



try:
    ENV_SETTINGS_MODE = load_credential('SETTINGS_MODE')
except ImproperlyConfigured:
    ENV_SETTINGS_MODE = 'dev'

if ENV_SETTINGS_MODE == 'prod':
    DEBUG = False
    # TODO
    DATABASES = {

    }
elif ENV_SETTINGS_MODE == 'travis':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'NAME': 'snuclub_travis',
            'USER': 'travis'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': load_credential('DEV_DATABASE_HOST'),
            'NAME': load_credential('DEV_DATABASE_NAME'),
            'USER': load_credential('DEV_DATABASE_USER'),
            'PASSWORD': load_credential('DEV_DATABASE_PASSWORD'),
            'PORT': '3314',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
        }
    }

if ENV_SETTINGS_MODE == 'dev':
    INSTALLED_APPS += [
        'rest_framework_swagger',
    ]
