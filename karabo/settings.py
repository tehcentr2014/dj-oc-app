"""
Django settings for karabo project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import os
import sys
from django.contrib import messages
import environ
from dotenv import load_dotenv
import dj_database_url
if os.path.isfile('env.py'):
    import env
# db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)



SECRET_KEY = 'django-insecure-1#jc!1ww4!7u8=h3i)yj_ob&#w8#osuyf&b1n1abpp*j3bvml1'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY 

#OPENAI_API_KEY = config('OPENAI_API_KEY')
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load environment variables from .env file
load_dotenv()

# Fetch the API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com', 'http://127.0.0.1:8000/', 'https://8000-tehcentr2014-djocapp-ip3vj2645q3.ws-eu114.gitpod.io/', '8000-tehcentr2014-djocapp-ip3vj2645q3.ws-eu115.gitpod.io', 'https://dj-oc-app-95fdf0716ca4.herokuapp.com','127.0.0.1', 'dj-oc-app-95fdf0716ca4.herokuapp.com']
CSRF_TRUSTED_ORIGINS = ['https://*.herokuapp.com', 'https://8000-tehcentr2014-djocapp-ip3vj2645q3.ws-eu115.gitpod.io', 'http://8000-tehcentr2014-djocapp-ip3vj2645q3.ws-eu114.gitpod.io/index.html', 'https://dj-oc-app-95fdf0716ca4.herokuapp.com']


DJANGO_SETTINGS_MODULE =['karabo.settings']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ##Third Party Apps
    'crispy_forms',
    'crispy_bootstrap5',
    #'crispy_bootstrap4',  # For Bootstrap 4 support
    # Created Apps
    'landing',
    'authorisation',
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'karabo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'karabo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {     
# 		'default': {
#       	'ENGINE': 'django.db.backends.postgresql',
#       	'HOST' : os.environ.get('POSTGRES_HOST', 'localhost'),
#       	'NAME': os.environ.get('POSTGRES_DB', 'db_name'),
#       	'USER': os.environ.get('POSTGRES_USER', 'username'),
#       	'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'),
#       	'PORT': os.environ.get('POSTGRES_PORT', '5432'),
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL")),
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'

DJANGORESIZED_DEFAULT_SIZE = [500, 500]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'PNG': ".png"}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/uploads/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tehcentr1920@gmail.com'
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'tehcentr1920@gmail.com'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
