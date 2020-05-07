import os
from app.settings.components.common import (
    ALLOWED_HOSTS
)

# Turn off debugging
DEBUG = False

ALLOWED_HOSTS += [
    'localhost',
    '127.0.0.1',
]

# Database configuration
DATABASES = {
    'default': {
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'ENGINE': 'django.db.backends.postgresql',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': '',
    }
}

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
