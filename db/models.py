from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from db.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(511), nullable=True)
    price = Column(DECIMAL, nullable=True)
    created_at = Column(DATETIME, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    category = relationship("Category", back_populates="products")
