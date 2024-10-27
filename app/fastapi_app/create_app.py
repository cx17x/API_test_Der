from fastapi import FastAPI

import uvicorn

from app.fastapi_app.views.routers.service import service_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(service_router)
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
