import asyncio

from fastapi import FastAPI

import uvicorn

from app.fastapi_app.common_router import main_router
from app.fastapi_app.sheduller.start_sheduller import scheduled_add_extention


def create_app() -> FastAPI:

    app = FastAPI()
    app.include_router(main_router)

    @app.on_event("startup")
    async def startup_event():
        asyncio.create_task(scheduled_add_extention())

    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
