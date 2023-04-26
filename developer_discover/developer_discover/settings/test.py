from .base import *

SECRET_KEY = "github_test_secret_key"
# DATABASE_URL="postgres://postgres:postgres@localhost:5432/test_db"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_db",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
