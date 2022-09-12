from pydantic import BaseModel

# TODO: all needs rethinking
class OfferBase(BaseModel):
    username: str


class OfferCreate(OfferBase):
    pass


class Offer(OfferBase):
    id: int

    class Config:
        orm_mode = True


class OfferResponse(BaseModel):
    success: bool
    offer_id: int
    user: Offer
    total_offers: int