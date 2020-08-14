from pydantic import BaseSettings

class Settings(BaseSettings):
    API_PREFIX: str = '/v1/api/'
    APP_NAME: str = 'Mimony API'


settings = Settings()