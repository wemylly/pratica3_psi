from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, criar_banco

class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[String] = mapped_column(String(80), nullable=False)
    email: Mapped[String] = mapped_column(String(80), unique=True)

    Books: Mapped[List["Book"]] = relationship(back_populates="Users")


class Book(Base):
    __tablename__ = "Book"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[String] = mapped_column(String(100), nullable=False)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("User.id"))

    Users: Mapped["User"] = relationship(back_populates="Books")

criar_banco()