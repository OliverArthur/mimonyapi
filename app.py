import uvicorn
from app.main import app
from app.core import config

if __name__ == '__main__':
    uvicorn.run(app, host=config.SERVER_NAME, port=config.SERVER_PORT, debug=True)
