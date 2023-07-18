from decouple import config

from .base import *

SECRET_KEY = "abc"  # for dev purpose only or create one by django-extensions

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ["*", "localhost"]
