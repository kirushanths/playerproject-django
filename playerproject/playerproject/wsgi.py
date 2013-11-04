"""
WSGI config for playerproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

# import os
# import sys
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playerproject.settings")

# APP_DIR = os.path.abspath(os.path.dirname(__file__)).replace('\\','/')
# sys.path.append(APP_DIR)
# print APP_DIR
# output = 'sys.path = %s' % repr(sys.path)
# print [output]

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# import uwsgi
# from uwsgidecorators import timer
# from django.utils import autoreload

# @timer(1)
# def change_code_gracefull_reload(sig):
#     if autoreload.code_changed():
#         uwsgi.reload()