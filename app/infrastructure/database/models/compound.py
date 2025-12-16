from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.infrastructure.database.models import BaseModelMixin

__all__ = ["Compound"]




class Compound(BaseModelMixin):
    __tablename__ = "compounds"

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    name_slug: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    description: Mapped[str | None] = mapped_column(String, nullable=True)

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    client = relationship("Client", back_populates="compounds")
    trials = relationship("Trial", back_populates="compound")