from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.infrastructure.database.models import BaseModelMixin

__all__ = ["Client"]


class Client(BaseModelMixin):
    __tablename__ = "clients"

    name: Mapped[str] = mapped_column(String(512), nullable=False, index=True)

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    company = relationship("Company", back_populates="clients")
    compounds = relationship("Compound", back_populates="client")
