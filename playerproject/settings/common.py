import os
from django.core.urlresolvers import reverse_lazy

# Django settings for dazzle project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

# Move up one folder cause we inside settings/
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_PATH, os.pardir)).replace('\\','/')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

AUTH_USER_MODEL = 'accounts.DZUser'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'aalk!vza-cq($cce!b@b$!%d^9%vrjxam-74&zv)i!e$=y9dd3rt=y'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'dazzle.apps.accounts.middleware.UpdateLastActivityMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dazzle.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'dazzle.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dazzle.apps',
    'dazzle.apps.api',
    'dazzle.apps.billing',
    'dazzle.apps.corporate',
    'dazzle.apps.accounts',
    'dazzle.apps.dashboard',
    'dazzle.apps.engine',
    'dazzle.apps.dztemplate',
    'dazzle.libs.model',
    'dazzle.libs.utils',
    'south',
    # 'storages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# LOGIN_REDIRECT_URL = '/accounts/dashboard/'
# LOGIN_URL = '/accounts/login/'
# LOGOUT_URL = '/accounts/logout/'

LOGIN_REDIRECT_URL = reverse_lazy('dashboard_home')
LOGIN_URL = reverse_lazy('account_login')
LOGOUT_URL = reverse_lazy('account_logout')

# S3 AMAZON

S3_ACCESS_KEY = 'AKIAIT5VHRH3SYEXEX5Q'
S3_SECRET_KEY = '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'
S3_URL = 'http://s3.amazonaws.com/'
S3_BUCKET = 'dazzledev'
S3_TEMPLATE_FOLDER = '/templates/'
S3_TEMPLATE_FOLDER_NAME = 'templates'
S3_TEMPLATE_URL = S3_URL + S3_BUCKET + S3_TEMPLATE_FOLDER

