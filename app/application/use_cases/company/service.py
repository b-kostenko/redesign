from app.application.use_cases.company.dto import CompanyCreateDTO, CompanyDTO
from app.application.use_cases.company.mapper import CompanyMapper
from app.domain.exceptions.company import CompanyAlreadyExistsError
from app.domain.interfaces import CompanyRepositoryInterface


class CompanyService:
    def __init__(self, repository: CompanyRepositoryInterface, domain: str):
        self.repository: CompanyRepositoryInterface = repository
        self.domain: str = domain

    @staticmethod
    def _prepare_slug(name: str) -> str:
        return name.lower().replace(" ", "-")

    def _prepare_domain(self, slug: str) -> str:
        return f"{slug}.{self.domain}"

    async def create_company(self, company_data: CompanyCreateDTO) -> CompanyDTO:
        slug = self._prepare_slug(company_data.name)
        domain = self._prepare_domain(slug)

        company_entity = CompanyMapper.dto_to_entity(company=company_data, company_slug=slug, company_domain=domain)

        company_exists = await self.repository.get_company_by_name(name=company_data.name)
        if company_exists:
            raise CompanyAlreadyExistsError(name=company_data.name)

        company = await self.repository.create_company(company_entity=company_entity)
        return CompanyMapper.entity_to_dto(company=company)

    async def get_company_by_domain(self, domain: str) -> CompanyDTO | None:
        company = await self.repository.get_company_by_domain(domain=domain)
        if not company:
            return None
        return CompanyMapper.entity_to_dto(company=company)
