import os
import environ

from pathlib import Path


# GENERAL
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)
env.read_env(BASE_DIR / '.env')

TIME_ZONE = env('TZ')
LANGUAGE_CODE = 'ja'

SITE_ID = 1

USE_I18N = True
USE_TZ = False

# DATABASES
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# APPS
DAJNGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
]
THIRD_PARTY_APPS=[
    'allauth',
    'allauth.account',
    'allauth.mfa',
    'allauth.socialaccount',
]
LOCAL_APPS=[]
INSTALLED_APPS=DAJNGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# AUTHENTICATION
# AUTHENTICATION_BACKENDS = []
# AUTH_USER_MODEL = ''
# LOGIN_REDIRECT_URL = ''
# LOGIN_URL = ''

# django-allauth
# ACCOUNT_ALLOW_REGISTRATION = True
# ACCOUNT_AUTHENTICATION_METHOD = ''
# ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_ADAPTER = ''
# ACCOUNT_FORMS = {}
# SOCIALACCOUNT_ADAPTER = ''
# SOCIALACCOUNT_FORMS = {}
