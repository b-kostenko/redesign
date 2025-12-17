from app.infrastructure.database.models import BaseModelMixin
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

__all__ = ["Client"]


class Client(BaseModelMixin):
    __tablename__ = "clients"

    name: Mapped[str] = mapped_column(String(512), nullable=False, index=True)

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    company = relationship("Company", back_populates="clients")
    compounds = relationship("Compound", back_populates="client")
