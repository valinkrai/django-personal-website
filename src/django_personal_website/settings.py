"""
Django settings for django_personal_website project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import uuid

# Determine if production or test server
PRODUCTION_UUIDS = [56817295373]

# Assume Dev if no prod flag
if os.environ.get('PROD') == 'true':
    PROD = True
else:
    PROD = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not PROD

ALLOWED_HOSTS = os.environ["DJANGO_SECRET_KEY"].split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'resume.apps.ResumeConfig',
    'projects.apps.ProjectsConfig',
    'social.apps.SocialConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_personal_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'django_personal_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if os.environ.get('DJANGO_POSTGRES'):
    print("DB: postgres docker is go")
    # settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db', # set in docker-compose.yml
            'PORT': 5432 # default postgres port
        }
    }
elif PROD:
    print("DB: postgres psycopg2 is go")
    with open(os.path.join(BASE_DIR, 'database.password')) as f:
        PROD_DB_PW = f.read().strip()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_personal_website',
            'USER': 'django',
            'PASSWORD': PROD_DB_PW,
            'HOST': 'db',
            'PORT': '',
        }
    }
else:
    print("DB: sqlite is go")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Central'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Final directory for serving static files
SRV_DIR = '/srv/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = (
    'static',
    os.path.join(BASE_DIR, 'static'),
)

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(SRV_DIR, 'static')

# Media files (Uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SRV_DIR, 'media')

# Security
if PROD:
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False ## Update later
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

# Email
DEFAULT_FROM_EMAIL = 'noreply@trenton.io'