from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.infrastructure.database.models import BaseModelMixin

__all__ = ["Trial"]


class Trial(BaseModelMixin):
    __tablename__ = "trials"

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    name_slug: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    description: Mapped[str | None] = mapped_column(String, nullable=True)

    compound_id: Mapped[int] = mapped_column(ForeignKey("compounds.id"), nullable=False)
    compound = relationship("Compound", back_populates="trials")