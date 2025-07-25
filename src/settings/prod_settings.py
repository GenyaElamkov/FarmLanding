import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY_PROD")

DEBUG = False

ALLOWED_HOSTS = ['elamkotk.beget.tech']

WSGI_APPLICATION = 'HelloDjango.wsgi.application'


STATIC_ROOT = '/home/e/elamkotk/farmlanding/public_html/static'

DATABASES = {
    "default": {
        "OPTIONS": {
                    "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
                    "sql_mode": "STRICT_TRANS_TABLES",
                   },
        "ENGINE": "django.db.backends.mysql",
        "NAME": "elamkotk_ecofarm",
        "USER": "elamkotk_ecofarm",
        "PASSWORD": "RK{DhXM6WO",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
