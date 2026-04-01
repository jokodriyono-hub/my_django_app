"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

# 1. Path ke folder UTAMA (yang ada manage.py)
path = '/home/jokodriyono/my_django_app' 
if path not in sys.path:
    sys.path.append(path)

# 2. Set environment module (Folder yang ada settings.py)
# Jika folder inti Anda bernama 'py_project_lgr01', maka:
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()