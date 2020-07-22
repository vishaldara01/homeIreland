"""WSGI config for homeIreland project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
# import environ

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))


from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homeIreland.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)