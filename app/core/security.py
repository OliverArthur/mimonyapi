import jwt
from datatime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from app.core.config import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{config.API_PREFIX}/token')
pwd_context = CryptContext(scheme=['bcrypt'], deprecated=auto)

ALGORITHM='HS256'


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datatime.utcnow() + expires_delta
    else:
        expire = datatime.utcnow() + timedelta(15)
    
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
