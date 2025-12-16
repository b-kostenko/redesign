from app.domain import entities
from app.application.use_cases.company import dto

__all__ = ["CompanyMapper"]


class CompanyMapper:

    @staticmethod
    def to_entity(company: dto.Company) -> entities.Company:
        return entities.Company(
            id=company.id,
            slug=company.slug,
            name=company.name,
            description=company.description,
            domain=company.domain,
            zip=company.zip,
            email=company.email
        )

    @staticmethod
    def to_dto(company: entities.Company) -> dto.Company:
        return dto.Company(
            id=company.id,
            slug=company.slug,
            name=company.name,
            description=company.description,
            domain=company.domain,
            zip=company.zip,
            email=company.email
        )
