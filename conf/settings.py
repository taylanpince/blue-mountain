DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bluemountain',
        'USER': 'bluemountaindbu',
        'PASSWORD': 'a0ahztlYj3',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_URL = '/media/'
