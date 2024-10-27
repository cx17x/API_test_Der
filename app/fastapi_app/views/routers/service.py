from fastapi import APIRouter, requests

service_router = APIRouter()


@service_router.get("/service")
def add():
    pass