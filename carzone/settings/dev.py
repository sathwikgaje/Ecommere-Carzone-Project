from ..settings import *

DEBUG = True

SECRET_KEY = 'u3b7-ti3qfmje1r@_fta^&9ygfw)j3$hc8)fa-9-*-v5zdu6vb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carzone_db',
        'USER' : 'postgres',
        'PASSWORD' : 'sahruday@1',
        'HOST' : 'localhost',
    }
}