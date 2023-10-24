from sqlalchemy.orm import Session

from category import schemas
from db import models


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


def get_all_categories(db: Session):
    return db.query(models.Category)


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(
        models.Category.id == category_id
    ).first()


def get_category_by_name(db: Session, name: str):
    return db.query(models.Category).filter(
        models.Category.name == name
    ).first()


def update_category(
        db: Session,
        category: models.Category,
        category_update: schemas.CategoryCreate
):
    for field, value in category_update.model_dump().items():
        if value is not None:
            setattr(category, field, value)

    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def delete_category(db: Session, category_id: int):
    category_to_delete = get_category(db, category_id)
    if category_to_delete is not None:
        db.delete(category_to_delete)
        db.commit()
        return category_to_delete
    return None
