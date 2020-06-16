from restapp.envs.base import *

SECRET_KEY = "(3gbc8!%m4t#t22(*edr=93z!3&uwpp!k2=-k-2&vf7g=5vo48"
DEBUG = True

DATABASES = {
    
    "local": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "comics",
        "USER": "postgres",
        "PASSWORD": "testingdb",
        "HOST": "localhost",
        "PORT": "5432",
        "TEST": {"NAME": "mytestdatabase",},
    },
}

DATABASES["default"] = DATABASES["local"]