from fastapi import FastAPI
from app.core import config


def create_app():
    api = FastAPI(title='Mimony API')

    @api.get('/')
    def root():
        return {"status": "ok"}

    return api

app = create_app()
