
import os
#from stripe import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = "/Users/jmitch/desktop/trydjango19/src/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sm@g)(fbwdh5wc*xe@j++m9rh^uza5se9a57c5ptwkg*b@ki0x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'warm-bayou-75381.herokuapp.com']

AUTHENTICATION_BACKENDS = ('trydjango19.backends.EmailAuthBackend',)


DEFAULT_FROM_EMAIL = 'praveenkumar.sayone@gmail.com'
SERVER_EMAIL = 'praveenkumar.sayone@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'praveenkumar.sayone@gmail.com'
EMAIL_HOST_PASSWORD = 'qwerty@123'

STRIPE_PUBLISHABLE = 'pk_test_ZQv3SAiAFPs4NDgNRjDWABJG'
STRIPE_SECRET = 'sk_test_jJkAZqFqrz03caYak2Un4ex7'
# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'inventory',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'trydjango19.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'trydjango19.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
]

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#herku
GOOGLE_RECAPTCHA_SITE_KEY = '6LfeXBYUAAAAAKn7Phs-remsu37EexY2tkmXlEhj'
GOOGLE_RECAPTCHA_SECRET_KEY = '6LfeXBYUAAAAAA0qWdqqea7TyLZCv0ipMDarmy2Q'

#localhost
#GOOGLE_RECAPTCHA_SITE_KEY = '6LeXfxQUAAAAAK-yPbVnuorXVn2nWPoZCzSbY-Gw'
#GOOGLE_RECAPTCHA_SECRET_KEY = '6LeXfxQUAAAAAIIvSfPPscuPLqQBGPdiEF5EB5FS'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

#LOGIN_URL = 'http://127.0.0.1:8000/inventory/login/'
LOGIN_URL = 'warm-bayou-75381.herokuapp.com/inventory/login/'

#stripe
#test keys
STRIPE_PUBLISHABLE_KEY = 'pk_test_ZQv3SAiAFPs4NDgNRjDWABJG'
STRIPE_SECRET_KEY = 'sk_test_jJkAZqFqrz03caYak2Un4ex7'

#live keys
# STRIPE_PUBLISHABLE_KEY = 'pk_live_moxDEabh9owhohAbPEjEoRt9'
# STRIPE_SECRET_KEY = 'sk_live_GOfz8qw54s86IbNTTWJ6FqzC'