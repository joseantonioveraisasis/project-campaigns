"""
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#         #'NAME': BASE_DIR.child('db.sqlite3'),
#     }
# }

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'OPTIONS': {
                'options': '-c search_path=public,campanias,development,temporal'
            },

        'NAME': 'local',

        'USER': 'postgres',

        'PASSWORD': 'contrasenia',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
  BASE_DIR / "../static/",
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

FILE_UPLOAD_HANDLERS = ["django.core.files.uploadhandler.MemoryFileUploadHandler",
 "django.core.files.uploadhandler.TemporaryFileUploadHandler"]


