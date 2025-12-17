from typing import Annotated

from app.application.use_cases.company.dto import CompanyDTO
from app.application.use_cases.company.service import CompanyService
from app.config.settings import settings
from app.infrastructure.database.repositories.company.mapper import CompanyMapper
from app.infrastructure.database.repositories.company.repository import CompanyRepositorySQLAlchemy
from app.infrastructure.database.session import create_async_session
from fastapi import HTTPException, Request
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


def get_company_mapper() -> CompanyMapper:
    return CompanyMapper()


def get_company_repository(
    company_mapper: CompanyMapper = Depends(get_company_mapper), session: AsyncSession = Depends(create_async_session)
) -> CompanyRepositorySQLAlchemy:
    return CompanyRepositorySQLAlchemy(session=session, mapper=company_mapper)


def get_company_service(
    repository: CompanyRepositorySQLAlchemy = Depends(get_company_repository),
) -> CompanyService:
    return CompanyService(repository=repository, domain=settings.app.DOMAIN)


def get_tenant_company(request: Request) -> CompanyDTO:
    if hasattr(request.state, "company_tenant"):
        return request.state.company_tenant
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tenant company not resolved",
    )


tenant_company_deps = Annotated[CompanyDTO, Depends(get_tenant_company)]

company_service_deps = Annotated[CompanyService, Depends(get_company_service)]
