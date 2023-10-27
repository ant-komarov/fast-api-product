from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from product import schemas, crud
from category import crud as c_crud
from db.dependencies import get_db

router = APIRouter(prefix="/products")


@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_name(db=db, name=product.name)
    db_category = c_crud.get_category(db=db, category_id=product.category_id)

    if db_category is None:
        raise HTTPException(
            status_code=400, detail=f"Category with id: {product.category_id} does not exists"
        )

    if db_product:
        raise HTTPException(
            status_code=400, detail="Product with such name already exists"
        )

    return crud.create_product(db=db, product=product)


@router.get("/", response_model=list[schemas.Product])
def get_products_list(db: Session = Depends(get_db)):
    return crud.get_all_products(db=db)


@router.get("/{product_id}/", response_model=schemas.Product)
def get_single_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_single_product(db=db, product_id=product_id)

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return db_product


@router.put("/{product_id}/", response_model=schemas.Product)
def update_product(
    product_id: int,
    product_update: schemas.ProductCreate,
    db: Session = Depends(get_db),
):
    existing_product = crud.get_single_product(db=db, product_id=product_id)
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = crud.update_product(
        db=db, product=existing_product, product_update=product_update.model_dump()
    )
    return updated_product


@router.delete("/{product_id}/")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_single_product(db=db, product_id=product_id)
    if product:
        crud.delete_product(db=db, product_id=product_id)
        return {"message": "product successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")
