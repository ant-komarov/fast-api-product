from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(examples=["Category"])


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True
