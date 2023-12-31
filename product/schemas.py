from datetime import datetime

from pydantic import BaseModel, Field, validator

from category import schemas


class ProductBase(BaseModel):
    name: str = Field(
        min_length=5, max_length=255, pattern=r"^[a-zA-Z0-9_ ]+$", examples=["Product"]
    )
    description: str = Field(max_length=511, examples=["Description"])
    price: float = Field(ge=0, examples=[9.99])
    quantity: int


class ProductCreate(ProductBase):
    category_id: int

    @validator("price")
    @classmethod
    def round_price(cls, value):
        return round(value, 2)


class Product(ProductBase):
    id: int
    created_at: datetime
    category: schemas.CategoryCreate

    class Config:
        from_attributes = True
