import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = 'errors@lovewinterturnblue.ca'
DEFAULT_FROM_EMAIL = 'no-reply@lovewinterturnblue.ca'

ADMINS = (
    ('Taylan Pince', 'taylanpince@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Canada/Eastern'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'

SITE_ID = 1

MEDIA_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media/')
MEDIA_URL = '/media/'

SECRET_KEY = 'dablw8qa8)p4bb6zx=$$o=x#7u)0&g#@_jo1810e$^wa=h-8_9'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

TEMPLATE_LOADERS = (
    'django_mobile.loader.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django_mobile.context_processors.flavour',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'bluemountain.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.realpath(os.path.dirname(__file__)), 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',

    'django_extensions',
    'django_mobile',
    'sorl.thumbnail',
    'south',

    'content_blocks',
    'contests',
    'events',
)

try:
    from settings_local import *
except:
    pass

ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
