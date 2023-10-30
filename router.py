from fastapi import APIRouter

from category import router as category_router
from product import router as product_router


router_v1 = APIRouter(prefix="/api/v1")


router_v1.include_router(category_router.router)
router_v1.include_router(product_router.router)
