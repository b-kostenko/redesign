from collections.abc import Awaitable, Callable

from app.application.use_cases.company.mapper import CompanyMapper as AppCompanyMapper
from app.domain.exceptions.company import CompanyNotFoundError
from app.infrastructure.database.repositories.company.mapper import CompanyMapper
from app.infrastructure.database.repositories.company.repository import CompanyRepositorySQLAlchemy
from app.infrastructure.database.session import SessionFactory
from app.presentation.api.exception_handlers import not_found_handler
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class CompanyTenantMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        host = request.headers.get("host")
        if host is None:
            return not_found_handler(request, CompanyNotFoundError(company_attr="unknown"))

        async with SessionFactory() as session:
            repo = CompanyRepositorySQLAlchemy(
                session=session,
                mapper=CompanyMapper(),
            )
            company = await repo.get_company_by_domain(company_domain=host)

            if company is None:
                return not_found_handler(request, CompanyNotFoundError(company_attr=host))

            request.state.company_tenant = AppCompanyMapper.entity_to_dto(company)

        response = await call_next(request)
        return response
