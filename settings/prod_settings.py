import os

import dj_database_url


# Pull database config from Heroku's dyno's environment variables using dj_database_url
DATABASES = {'default': dj_database_url.config()}

# For now, allow from all hosts
ALLOWED_HOSTS = ['*']

# Actual secret key should be pulled from Heroku
SECRET_KEY = os.getenv('SECRET_KEY', None)
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', None)
MEETUP_API_KEY = os.getenv('MEETUP_API_KEY', None)

# Why not GZIP and client-cache files?
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Update celery settings via Heroku environment variables
BROKER_URL = os.getenv('REDIS_URL', None)
CELERY_RESULT_BACKEND = os.getenv('REDIS_URL', None)
