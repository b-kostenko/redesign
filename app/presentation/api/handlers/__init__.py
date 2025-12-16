from fastapi import APIRouter

from app.presentation.api.handlers.user.handler import router as user_router
from app.presentation.api.handlers.company.handler import router as company_router

routers = APIRouter(prefix="/api/v1")

routers.include_router(user_router)
routers.include_router(company_router)

