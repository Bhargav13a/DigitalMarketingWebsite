"""
WSGI config for buzz_craft_socials project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'buzz_craft_socials.settings')

application = get_wsgi_application()


# add your project to the path
path = '/home/Bhargav13a/DigitalMarketingWebsite'
if path not in sys.path:
    sys.path.append(path)

# set DJANGO_SETTINGS_MODULE
os.environ['DJANGO_SETTINGS_MODULE'] = 'your_project_name.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
