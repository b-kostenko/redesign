from app.domain import entities
from app.infrastructure.database import models

__all__ = ["CompanyMapper"]


class CompanyMapper:

    @staticmethod
    def to_model(company_entity: entities.CompanyCreate) -> models.Company:
        return models.Company(
            name=company_entity.name,
            slug=company_entity.slug,
            description=company_entity.description,
            domain=company_entity.domain,
            zip=company_entity.zip,
            email=company_entity.email,
        )

    @staticmethod
    def to_entity(company: models.Company) -> entities.Company:
        return entities.Company(
            id=company.id,
            name=company.name,
            slug=company.slug,
            description=company.description,
            domain=company.domain,
            zip=company.zip,
            email=company.email,
        )
