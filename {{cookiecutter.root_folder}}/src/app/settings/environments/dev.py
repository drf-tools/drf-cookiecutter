import os
{%- if cookiecutter.infrastructure == 'gcp' %}
from google.oauth2 import service_account

from app.settings.components import BASE_DIR
{%- endif %}
from app.settings.components.common import (
    ALLOWED_HOSTS,
)

# development settings
DEBUG = True

ALLOWED_HOSTS += [
    'localhost',
    '127.0.0.1',
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'NAME': os.environ.get('DATABASE_NAME', 'basedrf'),
        'USER': os.environ.get('DATABASE_USER', 'basedrf'),
        'ENGINE': 'django.db.backends.postgresql',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'basedrf'),
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', 5432),
    }
}

# No need whitelist, all origins will be accepted
CORS_ORIGIN_ALLOW_ALL = True

{%- if cookiecutter.infrastructure == 'gcp' %}

# Google Storage for static files.
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'your-bucket-name'
GS_PROJECT_ID = 'your-project-id'

STATIC_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)
STATIC_ROOT = 'static/'

# Credential file should be located on the root folder.
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, '../credentials.json')
)
{%- endif %}
