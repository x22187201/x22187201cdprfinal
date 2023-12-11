"""
Django settings for mywebsite project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a*_asbjd*@mx69#jm1h!1q-k5r1ljqwlxqb35!j_2je^s@7f2d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS=['https://20c90619b6154bf5981a2ce2fbf6eb4f.vfs.cloud9.eu-west-1.amazonaws.com',
'https://x22187201cddemo--env.eba-jwt32wxq.eu-west-1.elasticbeanstalk.com']
ALLOWED_HOSTS=['x22187201cddemo--env.eba-jwt32wxq.eu-west-1.elasticbeanstalk.com',
'20c90619b6154bf5981a2ce2fbf6eb4f.vfs.cloud9.eu-west-1.amazonaws.com',
'172.31.45.147','34.255.59.254','54.228.123.3']


# Application definition

INSTALLED_APPS = [
    'dapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.staticfiles.middleware.StaticFilesMiddleware',
]

ROOT_URLCONF = 'mywebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mywebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'mydatabase',
        'USER':'postgres',
        'PASSWORD':'mydbpassword',
        'HOST':'x22187201db.chwlezgyi7rm.eu-west-1.rds.amazonaws.com',# RDS endpoint
        'PORT':'5432',# Adjust the port based on your RDS configuration
        }
}

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL ='/static/'
STATIC_ROOT =BASE_DIR /'static'
MEDIA_ROOT =BASE_DIR /'media'
MEDIA_URL ='/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/'
