"""
# Django settings for cnitie_2023 project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(env_file=str(BASE_DIR / "cnitie_2023" / ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
# ALLOWED_HOSTS = ['www.itie.cg']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'newsletter',
    'sorl.thumbnail',
    'easy_thumbnails',
    'tinymce',
    # 'suit_redactor',
    'django_bootstrap5',
    # 'django_icons',
    'blog',
    'data',

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

ROOT_URLCONF = 'cnitie_2023.urls'

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

WSGI_APPLICATION = 'cnitie_2023.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

LANGUAGE_CODE = 'fr-Fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_proj"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn", "static_root")

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "static_cdn", "media_root")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

NEWSLETTER_THUMBNAIL = 'sorl-thumbnail'

# NEWSLETTER_THUMBNAIL = 'easy-thumbnails'

NEWSLETTER_CONFIRM_EMAIL = False

# NEWSLETTER_RICHTEXT_WIDGET = "suit_redactor.widgets.Textarea"

NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"

SITE_ID = 1

JAZZMIN_SETTINGS = {
    "site_title": "ITIE Congo",
    "site_header": "ITIE Congo",
    "site_brand": 'ITIE Congo',
    "site_logo": BASE_DIR.joinpath('static_proj/assets/logo/Logo_comite_national_mini.png'),
    "login_logo": BASE_DIR.joinpath('static_proj/assets/logo/Logo_comite_national_mini.png'),
    "site_icon": BASE_DIR.joinpath('static_proj/assets/img/RC.png'),
    "welcome_sign": "Bienvenu sur ITIE-CONGO-ADMIN",
    "search_model": ["blog.Post"],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "blog.Post": 'fa fa-blog',
        "newsletter.Newsletter": "fas fa-newspaper",
        "newsletter.Message": "fas fa-envelope",
        "newsletter.Subscription": "fas fa-plus",
        "newsletter.Submission": "fas fa-envelope-open",
        "sites.Site": "fas fa-globe",
        "flatpages.Flatpage": "fas fa-database"

    }
}
