"""
Django settings for cctvCameraproject project.
"""

from pathlib import Path
import os



# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--x7qow1tugob2)p+2seog#xwq@xj3ju$qvtmgl0=q+0r@e14m+'

DEBUG = False
ALLOWED_HOSTS = ['cctv-camera-project-2.onrender.com','*']



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cameraapp',
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

ROOT_URLCONF = 'cctvCameraproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templest')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cctvCameraproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cctv_db_ghv2',
        'USER': 'cctv_user',
        'PASSWORD': 'wVL3xRSTOzQ3N4lHpgmmtdCm7iWp9TZh',
        'HOST': 'dpg-d6l72nntskes73ej138g-a',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}
  






AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# Static files (CSS, JavaScript, Images)




from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',       
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'






DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = 'saurabhdhage20114@gmail.com'
# EMAIL_HOST_PASSWORD = 'wcqxaafxktkmwwyf'




# import ssl
# import certifi

# ssl._create_default_https_context = ssl._create_unverified_context







