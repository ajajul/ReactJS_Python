"""
WSGI config for giveback_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv

from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

from django.core.wsgi import get_wsgi_application

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'giveback_project.settings.live')

application = Sentry(get_wsgi_application())
