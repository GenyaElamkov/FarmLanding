import os
import sys


site_user_root_dir = '/home/e/elamkotk/farmlanding/public_html'
sys.path.insert(0, site_user_root_dir + '/HelloDjango')
sys.path.insert(1, site_user_root_dir + '/venv/lib/python3.11/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HelloDjango.settings')

from django.core.wsgi import get_wsgi_application  # noqa


application = get_wsgi_application()
