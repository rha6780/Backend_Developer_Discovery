import environ

from .base import *

environ.Env.read_env(BASE_DIR.parent / ".envs" / ".dev")

SECRET_KEY = env("SECRET_KEY")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

GITHUB_ID = env("GITHUB_ID")
GITHUB_SECRET = env("GITHUB_SECRET")
