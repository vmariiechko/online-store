import os
from .base import *
from ..env_utils import get_env

DEBUG = False
SECRET_KEY = get_env("DJANGO_SECRET_KEY")
STATIC_URL = get_env("DJANGO_STATIC_URL")
