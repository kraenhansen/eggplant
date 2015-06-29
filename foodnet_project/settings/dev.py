"""
Default settings for development
"""
from .base import *  # @UnusedWildImport
import sys

DEBUG = True

SECRET_KEY = 'BLAH BLAH BLAH'

# Show all console output
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['loggers']['foodnet']['level'] = 'DEBUG'

# Use SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.sqlite',
    }
}

SITE_ID = 1
DEFAULT_HTTP_PROTOCOL = 'http'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'username'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = '[FoodNet]'
EMAIL_TIMEOUT = 5
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'info@localhost'
SERVER_EMAIL = 'django@localhost'

ADMINS = ()


os.environ['RECAPTCHA_TESTING'] = 'True'

INSTALLED_APPS += ('debug_toolbar',)
INSTALLED_APPS += ('django_extensions',)

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

# The Django Debug Toolbar will only be shown to these client IPs.
INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.33.1',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'HIDE_DJANGO_SQL': False,
}


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--verbosity=2',
    '--stop',
    '--with-yanc',
#    '--cover-branches',
#    '--with-coverage',
#    '--cover-erase',
#    '--cover-package=foodnet',
    'foodnet',
]

for arg in sys.argv:
    if arg.startswith('--tests='):
        NOSE_ARGS = [
            '--verbosity=2',
            '--stop',
            '--with-yanc',
        ]
        break