from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db import Model


class Product(Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    manufacturer_id: Mapped[int] = mapped_column(
        ForeignKey("manufacturers.id"), index=True
    )  # naming convention: <referenced-entity>_id
    year: Mapped[int] = mapped_column(index=True)
    country: Mapped[str] = mapped_column(String(32))
    cpu: Mapped[str] = mapped_column(String(32))

    def __repr__(self):
        return f"Product({self.id}, '{self.name}')"


class Manufacturer(Model):
    __tablename__ = "manufacturers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)

    def __repr__(self):
        return f"Manufacturer({self.id}, '{self.name}')"
