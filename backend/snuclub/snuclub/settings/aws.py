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

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': load_credential('DEV_DATABASE_HOST'),
            'NAME': load_credential('DEV_DATABASE_NAME'),
            'USER': load_credential('DEV_DATABASE_USER'),
            'PASSWORD': load_credential('DEV_DATABASE_PASSWORD'),
            'PORT': '3314'
        }
    }
