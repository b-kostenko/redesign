from app.domain import entities
from app.infrastructure.database import models

__all__ = ["ClientMapper"]


class ClientMapper:

    @staticmethod
    def entity_to_model(entity: entities.ClientCreateEntity) -> models.Client:
        return models.Client(
            name=entity.name,
            company_id=entity.company_id,
        )

    @staticmethod
    def model_to_entity(model: models.Client) -> entities.ClientEntity:
        return entities.ClientEntity(
            id=model.id,
            name=model.name,
            company_id=model.company_id,
        )
