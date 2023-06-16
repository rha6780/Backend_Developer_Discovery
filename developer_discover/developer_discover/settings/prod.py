import environ

from .base import *

# environ.Env.read_env(BASE_DIR.parent / ".envs" / ".prod")

SECRET_KEY = os.environ["SECRET_KEY"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_PORT"],
    }
}


EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_PORT = 465
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
ACCOUNT_EMAIL_VERIFICATION = 'none'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


STATIC_ROOT = os.path.join(BASE_DIR, 'static')