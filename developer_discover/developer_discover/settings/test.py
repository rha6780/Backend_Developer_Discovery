from .base import *

SECRET_KEY = "github_test_secret_key"
DATABASE_URL="postgres://postgres:postgres@localhost:5432/github_actions"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "github_actions",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
