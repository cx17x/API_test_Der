from fastapi import APIRouter

service_router = APIRouter()


@service_router.get('/service')
def get_external():
    pass
