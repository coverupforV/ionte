import uvicorn

from uvicorn import run

from api import app


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)
