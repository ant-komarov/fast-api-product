from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from category import schemas, crud
from db.dependencies import get_db

router = APIRouter(prefix="/categories")


@router.post("/", response_model=schemas.Category)
def create_category(
        category: schemas.CategoryCreate,
        db: Session = Depends(get_db)
):
    db_category = crud.get_category_by_name(db=db, name=category.name)

    if db_category:
        raise HTTPException(
            status_code=400, detail="Category with such name already exists"
        )

    return crud.create_category(db=db, category=category)


@router.get("/", response_model=list[schemas.Category])
def get_categories_list(db: Session = Depends(get_db)):
    return crud.get_all_categories(db=db)


@router.get("/{category_id}/", response_model=schemas.Category)
def get_single_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db=db, category_id=category_id)

    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return db_category


@router.put("/{category_id}/", response_model=schemas.Category)
def update_category(
        category_id: int,
        category_update: schemas.CategoryCreate,
        db: Session = Depends(get_db)
):
    existing_category = crud.get_category(db=db, category_id=category_id)
    if existing_category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    updated_category = crud.update_category(
        db=db,
        category=existing_category,
        category_update=category_update
    )
    return updated_category


@router.delete("/{category_id}/")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db=db, category_id=category_id)
    if category:
        crud.delete_category(db=db, category_id=category_id)
        return {"message": "category successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Category not found")
