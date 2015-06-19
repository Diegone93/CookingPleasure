import os.path

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
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin'
)
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'website/templates')
)
