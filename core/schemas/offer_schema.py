from typing import List

from pydantic import BaseModel

from core.models import offer_models


class OfferBase(BaseModel):
    offer_id: int
    version_id: int
    product: str
    quantity: int
    price: float
    action_id: int
    action: offer_models.OfferActionEnum
    buyer_id: int
    buyer_state: offer_models.OfferStatesEnum
    buyer_private_data: dict
    seller_id: int
    seller_state: offer_models.OfferStatesEnum
    seller_private_data: dict

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


class OfferHistoryItem(BaseModel):
    pass


class OfferHistoryResponse(BaseModel):
    success: bool
    offer_id: int
    offer_history: List[OfferHistoryItem]
    offer_count: int


# ==================
#  Response Schemas
# ==================

class OfferResponse(BaseModel):
    success: bool
    created: int
    offer: Offer

 
class OfferCreateResponse(OfferResponse):
    pass

class OfferAcceptResponse(OfferResponse):
    pass

class OfferCancelResponse(OfferResponse):
    pass

class OfferWithdrawResponse(OfferResponse):
    pass
