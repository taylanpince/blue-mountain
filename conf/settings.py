DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bluemountain_production',
        'USER': 'bluemountaindbu',
        'PASSWORD': 'a0ahztlYj3',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_URL = 'http://media2.lovewinterturnblue.ca/'

CONTACT_EMAIL = 'contest@bluemountain.ca'
