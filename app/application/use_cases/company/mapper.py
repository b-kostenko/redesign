from app.application.use_cases.company.dto import CompanyCreateDTO, CompanyDTO
from app.domain import entities

__all__ = ["CompanyMapper"]


class CompanyMapper:

    @staticmethod
    def dto_to_entity(company: CompanyCreateDTO, company_slug: str, company_domain: str) -> entities.CompanyCreate:
        return entities.CompanyCreate(
            slug=company_slug,
            name=company.name,
            description=company.description,
            domain=company_domain,
            zip=company.zip,
            email=company.email,
        )

    @staticmethod
    def entity_to_dto(company: entities.Company) -> CompanyDTO:
        return CompanyDTO(
            id=company.id,
            slug=company.slug,
            name=company.name,
            description=company.description,
            domain=company.domain,
            zip=company.zip,
            email=company.email,
        )
