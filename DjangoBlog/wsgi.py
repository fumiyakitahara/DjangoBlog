"""
WSGI config for DjangoBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#DJANGO_SETTINGS_MODULEが各種の設定情報がどこにあるか教えている
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoBlog.settings')

application = get_wsgi_application()#wsgiを実行するための関数
