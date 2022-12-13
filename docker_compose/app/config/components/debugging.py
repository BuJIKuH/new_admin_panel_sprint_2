from config.components import installed_apps, middleware
from config.settings import DEBUG


if DEBUG:
    installed_apps.INSTALLED_APPS += ['debug_toolbar']
    middleware.MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
