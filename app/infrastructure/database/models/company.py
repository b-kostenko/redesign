from app.infrastructure.database.models import BaseModelMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

__all__ = ["Company"]


class Company(BaseModelMixin):
    __tablename__ = "companies"

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    description: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    domain: Mapped[str] = mapped_column(String(150), nullable=False)
    zip: Mapped[str] = mapped_column(String(20), nullable=True)
    email: Mapped[str] = mapped_column(String(150), nullable=True)

    users = relationship("User", back_populates="company")
    clients = relationship("Client", back_populates="company")

    def __repr__(self) -> str:
        return f"<Company(id={self.id}, name='{self.name}')>"
