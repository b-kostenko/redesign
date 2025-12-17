from app.presentation.api.handlers.auth.handler import router as auth_router
from app.presentation.api.handlers.client.handler import router as client_router
from app.presentation.api.handlers.company.handler import router as company_router
from app.presentation.api.handlers.user.handler import router as user_router
from fastapi import APIRouter

routers = APIRouter(prefix="/api/v1")

routers.include_router(user_router)
routers.include_router(company_router)
routers.include_router(auth_router)
routers.include_router(client_router)
