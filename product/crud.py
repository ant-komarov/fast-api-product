from datetime import datetime

from sqlalchemy.orm import Session

from db import models
from product import schemas


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(created_at=datetime.now(), **product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_all_products(db: Session):
    return db.query(models.Product)


def get_single_product(db: Session, product_id: int):
    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()


def get_product_by_name(db: Session, name: str):
    return db.query(models.Product).filter(
        models.Product.name == name
    ).first()


def update_product(
        db: Session,
        product: models.Product,
        product_update: dict
):
    for field, value in product_update.items():
        if value is not None:
            setattr(product, field, value)

    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int):
    product_to_delete = get_single_product(db, product_id)
    if product_to_delete is not None:
        db.delete(product_to_delete)
        db.commit()
        return product_to_delete
    return None
