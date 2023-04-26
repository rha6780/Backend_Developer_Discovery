from .base import *

SECRET_KEY = "github_test_secret_key"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_db",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": "5432",
    }
}
