import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config.logging import logger

from app.config.settings import settings
from app.presentation.api.handlers import routers
from app.presentation.middlewares.company_tenant import CompanyTenantMiddleware


def _include_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(
        CompanyTenantMiddleware
    )


def _include_error_handlers(app: FastAPI) -> None:
    pass

def _include_router(app: FastAPI) -> None:
    app.include_router(routers)

def create_app() -> FastAPI:
    app = FastAPI()
    _include_middleware(app)
    _include_router(app)
    _include_error_handlers(app)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.app.HOST,
        port=settings.app.PORT,
        reload=settings.app.DEBUG,
        log_config=None
    )