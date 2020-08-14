from fastapi import FastAPI

from .config import settings

def create_app():
    api = FastAPI(
        title=settings.APP_NAME,
        openapi_url=f'{settings.API_PREFIX}/openapi.json'
    )

    @api.get('/')
    async def index():
        return {"status": "ok"}
    return api


app = create_app()
