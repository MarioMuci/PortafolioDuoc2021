import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db./sqlite/sqlite3'),
    }
}

ORACLE = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/xe',
        'USER': 'C##PROYECTO',
        'PASSWORD': '12345',
    'NAME': 'xe',
        'HOST': 'localhost',
        'PORT': '1521',
    }
}