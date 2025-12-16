from sqlalchemy.ext.asyncio import AsyncSession
from app.domain import entities
from app.domain.interfaces import CompanyRepositoryInterface
from app.infrastructure.database.models import Company
from app.infrastructure.database.repositories.company.mapper import CompanyMapper
from sqlalchemy import select

class CompanyRepositorySQLAlchemy(CompanyRepositoryInterface):

    def __init__(self, session: AsyncSession, mapper: CompanyMapper):
        self.session: AsyncSession = session
        self.mapper: CompanyMapper = mapper

    async def get_company_by_name(self, company_name: str):
        pass

    async def get_company_by_domain(self, company_domain: str) -> entities.Company | None:
        query = select(Company).where(Company.domain == company_domain)
        result = await self.session.execute(query)
        company_model = result.scalars().first()
        if not company_model:
            return None
        return self.mapper.to_entity(company_model)


    async def create_company(self, company_entity: entities.Company) -> entities.Company:
        company_model = self.mapper.to_model(company_entity)
        self.session.add(company_model)
        await self.session.commit()
        await self.session.refresh(company_model)
        return self.mapper.to_entity(company_model)
