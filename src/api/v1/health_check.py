# py imports
from http import HTTPStatus

# fastapi imports
from fastapi import APIRouter

router = APIRouter()

@router.get('', status_code=HTTPStatus.OK)
async def health_check():
    return {}