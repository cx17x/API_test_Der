from fastapi import APIRouter

from app.fastapi_app.views import add_extention, db_getter

main_router = APIRouter()

main_router.include_router(
    db_getter.db_getter,
    prefix='/db_getter'
)