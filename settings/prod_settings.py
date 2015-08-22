import os
import dj_database_url

__author__ = 'zachmccormick'

# Pull database config from Heroku's dyno's environment variables using dj_database_url
DATABASES = {'default': dj_database_url.config()}

# For now, allow from all hosts
ALLOWED_HOSTS = ['*']

# Actual secret key should be pulled from Heroku
SECRET_KEY = os.getenv('SECRET_KEY', None)
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', None)

# Why not GZIP and client-cache files?
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
