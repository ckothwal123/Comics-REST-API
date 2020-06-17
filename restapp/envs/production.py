from restapp.envs.base import *
import dj_database_url

ALLOWED_HOSTS = ['*']

SECRET_KEY = "(3gbc8!%m4t#t22(*edr=93z!3&uwpp!k2=-k-2&vf7g=5vo48"
DEBUG = False
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# DATABASES = {

#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         # "NAME": "comics",
#         # "USER": "postgres",
#         # "PASSWORD": "testingdb",
#         # "HOST": "localhost",
#         # "PORT": "5432",
#         # "TEST": {"NAME": "mytestdatabase",},
#     },
# }