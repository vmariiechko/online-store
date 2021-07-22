import os
from .base import *
from ..env_utils import get_env
from dj_database_url import config

DEBUG = bool(get_env("DJANGO_DEBUG"))
SECRET_KEY = get_env("DJANGO_SECRET_KEY")
STATIC_URL = get_env("DJANGO_STATIC_URL")
ALLOWED_HOSTS = get_env("DJANGO_ALLOWED_HOSTS").split(",")

DATABASES['default'].update(config(conn_max_age=600))
