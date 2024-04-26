# py imports

# fastapi imports
from fastapi import APIRouter

# app imports
from .v1 import health_check

api_router = APIRouter()
api_router.include_router(health_check.router, prefix='/health-check', tags=['health-check'])