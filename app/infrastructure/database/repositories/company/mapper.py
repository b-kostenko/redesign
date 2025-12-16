from app.domain import entities
from app.infrastructure.database import models


__all__ = ["CompanyMapper"]


class CompanyMapper:

    def to_model(self, company_entity: entities.Company) -> models.Company:
        return models.Company(
            name=company_entity.name,
            slug=company_entity.slug,
            description=company_entity.description,
            domain=company_entity.domain,
            zip=company_entity.zip,
            email=company_entity.email
        )

    def to_entity(self, company: models.Company) -> entities.Company:
        return entities.Company(
            id=company.id,
            name=company.name,
            slug=company.slug,
            description=company.description,
            domain=company.domain,
            zip=company.zip,
            email=company.email
        )