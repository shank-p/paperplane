# fastapi imports
from fastapi import FastAPI

# app imports
from api.base import api_router
from core.config import settings


def include_router(app: FastAPI):
    app.include_router(api_router)

def start_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app


app = start_app()