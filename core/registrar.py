from fastapi import FastAPI

from app.api.router import router as app_router


def register_app() -> FastAPI:
    app = FastAPI()

    app.include_router(app_router)

    return app
