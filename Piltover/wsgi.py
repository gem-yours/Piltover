"""
WSGI config for Piltover project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

project_path = '/code/'
sys.path.append(project_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Piltover.settings')

application = get_wsgi_application()
