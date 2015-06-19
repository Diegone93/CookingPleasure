import os.path

ALLOWED_HOSTS = ['www.example.com']
DEBUG = True
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CookingPleasure',
        'USER': 'developeraccess',
        'PASSWORD': 'developeraccess',
    }
}
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'CookingPleasure.urls'
WSGI_APPLICATION = 'CookingPleasure.wsgi.application'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin'
)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's_vhwve^l#=*$(eug)!lolltv@4p3*vblgf4!)juqs!igh^!ib'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_URL = '/static/'