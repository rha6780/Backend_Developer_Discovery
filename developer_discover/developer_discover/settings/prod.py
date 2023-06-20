import environ

from .base import *

environ.Env.read_env(BASE_DIR.parent / ".envs" / ".prod")

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


STATIC_ROOT = os.path.join(BASE_DIR, 'static')