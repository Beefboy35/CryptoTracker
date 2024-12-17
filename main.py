from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from uvicorn import run

from src.routes.routes import ext_api

api = FastAPI()
api.include_router(ext_api)
api.mount("/static", StaticFiles(directory="src/static"))

# if __name__ == "__main__":
#     run("main:api", host="localhost", port=7321, reload=True)
