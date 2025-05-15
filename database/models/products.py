from sqlalchemy import ForeignKey, String, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from .categories import Categories

class Products(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str]
    image: Mapped[str] = mapped_column(String(255))
    price: Mapped[DECIMAL] = mapped_column(DECIMAL(5, 2))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    product_category: Mapped["Categories"] = relationship(back_populates='products')

    def __str__(self):
        return self.product_name
