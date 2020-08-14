import secrets
from envparse import env
from dotenv import load_dotenv

load_dotenv(verbose=True)

# app
APP_NAME = env.str("APP_NAME", default="Mimony")
APP_ENV = env.str("APP_ENV", default="development")
APP_DEBUG = env.bool("APP_DEBUG", default=True)

# api
API_PREFIX = env.str("API_PREFIX", default="/v1/api")

# server
SERVER_NAME = env.str("SERVER_NAME", default="0.0.0.0")
SERVER_HOST = env.str("SERVER_HOST", default="0.0.0.0")
SERVER_PORT = env.int("SERVER_PORT", default=8000)

# cors
CORS_ORIGINS = env.str("CORS_ORIGINS", default="0.0.0.0")

# DB
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL", default="sqlite:///./sqlite.db")

# sqlite need special parameters
if SQLALCHEMY_DATABASE_URI.startswith("sqlite"):
    SQLALCHEMY_CONNECT_ARGS = {"check_same_thread": False}
else:
    SQLALCHEMY_CONNECT_ARGS = {}  # pragma: no cover

# mail
SMTP_TLS = env.bool("SMTP_TLS", default=True)
SMTP_PORT = env.int("SMTP_PORT", default=587)
SMTP_HOST = env.str("SMTP_HOST", default="localhost")
SMTP_USER = env.str("SMTP_USER", default="root")
SMTP_PASSWORD = env.str("SMTP_PASSWORD", default="Test1234x")
EMAILS_FROM_EMAIL = env.str("EMAILS_FROM_EMAIL", default="root@localhost")
EMAILS_FROM_NAME = APP_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = env.int("EMAIL_RESET_TOKEN_EXPIRE_HOURS", default=24)
EMAIL_CONFIRMATION_TOKEN_EXPIRE_HOURS = env.int("EMAIL_CONFIRMATION_TOKEN_EXPIRE_HOURS", default=24)
EMAIL_TEMPLATES_DIR = "app/email-templates/build"
EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL


# security
MIN_PASSWORD_LENGTH = env.int("MIN_PASSWORD_LENGTH", default=8)
SECRET_KEY = env.str("SECRET_KEY", default=secrets.token_urlsafe(32))
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
PASSWORD_DB = env.str("PASSWORD_DB", default="mimony")