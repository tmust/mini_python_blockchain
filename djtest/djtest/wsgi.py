"""
WSGI config for djtest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from p2ptest.p2p import p2p
p2p.grpcNetworkStart()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djtest.settings")

application = get_wsgi_application()

