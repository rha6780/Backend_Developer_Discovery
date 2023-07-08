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

EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = 465
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
ACCOUNT_EMAIL_VERIFICATION = 'none'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


CSRF_TRUSTED_ORIGIN="localhost:3000"

# AWS
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

S3_MEDIA_PATH = "media/dev/"
