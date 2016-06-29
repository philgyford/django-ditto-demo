from .defaults import *

# Some changed settings for development.


DEBUG = True

CACHES = {
    'default': {
        # Use dummy cache (ie, no caching):
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',

        # Or use local memcached:
        #'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        #'LOCATION': '127.0.0.1:11211',
        #'TIMEOUT': 500, # millisecond
    }
}

# Debug Toolbar settings.
if DEBUG:
    MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    INSTALLED_APPS += ['debug_toolbar', ]
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        # Force the toolbar to show as INTERNAL_IPS wasn't working with Vagrant.
        'SHOW_TOOLBAR_CALLBACK': "%s.true" % __name__
    }
    INTERNAL_IPS = ['127.0.0.1', '192.168.33.1', '0.0.0.0']
    RESULTS_CACHE_SIZE = 100

    def true(request):
        return True

