from .base import *

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://edith-stein-schule.net'

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
