from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

from app.infrastructure.database.repositories.company.mapper import CompanyMapper
from app.infrastructure.database.repositories.company.repository import CompanyRepositorySQLAlchemy
from app.infrastructure.database.session import SessionFactory


class CompanyTenantMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        host = request.headers.get("host")

        async with SessionFactory() as session:
            repo = CompanyRepositorySQLAlchemy(
                session=session,
                mapper=CompanyMapper(),
            )
            company = await repo.get_company_by_domain(company_domain=host)

            request.state.company_tenant = company

        response = await call_next(request)
        return response
