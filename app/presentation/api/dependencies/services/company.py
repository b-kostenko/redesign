from typing import Annotated

from starlette import status

from app.domain import entities
from fastapi.params import Depends
from fastapi import Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.repositories.company.mapper import CompanyMapper
from app.application.use_cases.company.service import CompanyService
from app.infrastructure.database.repositories.company.repository import CompanyRepositorySQLAlchemy
from app.infrastructure.database.session import create_async_session


def get_company_mapper() -> CompanyMapper:
    return CompanyMapper()


def get_company_repository(
        company_mapper: CompanyMapper = Depends(get_company_mapper),
        session: AsyncSession = Depends(create_async_session)
) -> CompanyRepositorySQLAlchemy:
    return CompanyRepositorySQLAlchemy(session=session, mapper=company_mapper)


def get_company_service(
        repository: CompanyRepositorySQLAlchemy = Depends(get_company_repository),
) -> CompanyService:
    return CompanyService(repository=repository)


def get_tenant_company(request: Request):
    if hasattr(request.state, "company_tenant"):
        return request.state.company_tenant
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tenant company not resolved",
    )



tenant_company_deps = Annotated[entities.Company, Depends(get_tenant_company)]

company_service_deps = Annotated[CompanyService, Depends(get_company_service)]
