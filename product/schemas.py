from datetime import datetime

from pydantic import BaseModel

from category import schemas


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class ProductCreate(ProductBase):
    category_id: int


class ProductUpdate(ProductBase):
    name: str = None
    description: str = None
    price: float = None
    quantity: int = None
    category_id: int = None


class Product(ProductBase):
    id: int
    created_at: datetime
    category: schemas.Category

    class Config:
        from_attributes = True
