from fastapi import APIRouter

from .users import user_router
from .offers import offer_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(user_router)
v1_router.include_router(offer_router)
