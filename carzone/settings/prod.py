from carzone.settings.dev import DATABASES
from .common import *
import dj_database_url

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['ecommere-carzone-project.herokuapp.com']

DATABASES = {
    'default' : dj_database_url.config()
}