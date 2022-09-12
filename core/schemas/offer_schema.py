from pydantic import BaseModel
from core.models import offer_models


class OfferBase(BaseModel):
    product: str
    quantity: int
    price: float
    action_id: int
    action: offer_models.OfferActionEnum
    buyer_id: int
    buyer_state: offer_models.OfferStatesEnum
    seller_id: int
    seller_state: offer_models.OfferStatesEnum
    seller_private_data: dict
    buyer_private_data: dict

    class Config:  
        use_enum_values = True


class OfferCreate(BaseModel):
    product: str
    quantity: int
    price: float
    buyer_id: int
    seller_id: int
    buyer_private_data: dict


class Offer(OfferBase):
    id: int
    offer_id: int
    version_id: int

    class Config:
        orm_mode = True


# class OfferResponse(BaseModel):
#     success: bool
#     offer_id: int
#     user: Offer
#     total_offers: int