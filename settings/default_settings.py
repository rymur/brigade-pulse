import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# In production, we'll override this with a key stored in local.py
SECRET_KEY = '6s=km)xm-kt-xo#l-a+ei4am016_=u=$@90jsxebkve8l49la0'

DEBUG = True
TEMPLATE_DEBUG = True

# In production, we'll override this with '.brigadepulse.com'
ALLOWED_HOSTS = []

# Application definitions.  We'll keep separate 3rd party and our apps.
THIRD_PARTY_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

OUR_APPS = (
    'api',
)

INSTALLED_APPS = THIRD_PARTY_APPS + OUR_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'settings.wsgi_settings.application'


# We'll use Postgres for both local and production!

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'brigadepulse',
        'USER': 'brigadepulse',
        'PASSWORD': 'brigadepulse',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# We'll force all timestamps to be saved and served in UTC, regardless of client/host timezone
TIME_ZONE = 'UTC'
USE_TZ = False


# DjangoWhiteNoise requires STATIC_URL and STATIC_ROOT to be set even though we don't really use them.
# TEMPLATE_DIRS allows us to serve index.html at the root + WHITENOISE_ROOT allows us to serve files
# from the public directory directly.  Probably not *best* practice, but it works for us.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'public'),)
WHITENOISE_ROOT = os.path.join(BASE_DIR, 'public')