ALLOWED_HOSTS = ['www.example.com']
DEBUG = True
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CookingPleasure',
        'USER': 'developerAccess',
        'PASSWORD': 'developeraccess',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
