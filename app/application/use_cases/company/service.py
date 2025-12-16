from app.application.use_cases.company.mapper import CompanyMapper
from app.domain.interfaces import CompanyRepositoryInterface
from app.application.use_cases.company import dto


class CompanyService:
    def __init__(self, repository: CompanyRepositoryInterface, domain: str):
        self.repository: CompanyRepositoryInterface = repository
        self.domain: str = domain

    @staticmethod
    def _prepare_slug(name: str) -> str:
        return name.lower().replace(" ", "-")

    def _prepare_domain(self, slug: str) -> str:
        return f"{slug}.{self.domain}"

    async def create_company(self, company_data: dto.Company) -> dto.Company:
        company_entity = CompanyMapper.to_entity(company=company_data)
        company_entity.slug = self._prepare_slug(company_data.name)
        company_entity.domain = self._prepare_domain(company_entity.slug)

        company = await self.repository.create_company(company_entity=company_entity)
        return CompanyMapper.to_dto(company=company)

    async def get_company_by_domain(self, domain: str) -> dto.Company | None:
        company = await self.repository.get_company_by_domain(domain=domain)
        if not company:
            return None
        return CompanyMapper.to_dto(company=company)
