import enum

from sqlalchemy import JSON, Column, Float, ForeignKey, Integer, String
from sqlalchemy.types import Enum

from ..database import Base


class OfferStatesEnum(enum.Enum):
    awaiting_my_acceptance = "AwaitingMyAcceptance"
    awaiting_their_acceptance = "AwaitingTheirAcceptance"
    withdrawn_by_me = "WithdrawnByMe"
    withdrawn_by_them = "WithdrawnByThem"
    accepted = "Accepted"
    cancelled = "Cancelled"


class OfferActionEnum(enum.Enum):
    submit = "Submit"
    accept = "Accept"
    cancel = "Cancel"
    propose_update = "ProposeUpdate"
    withdraw = "Withdraw"
    update_private_data = "UpdatePrivateData"


class Offer(Base):
    __tablename__ = "offer"

    id = Column(Integer, primary_key=True, index=True)

    # Offer information
    offer_id = Column(Integer)
    version_id = Column(Integer, default=1)
    product = Column(String)
    quantity = Column(Integer)
    price = Column(Float)

    # Action logged
    action_id = Column(Integer, ForeignKey("user.id"))
    action = Column(Enum(OfferActionEnum))

    # Buyer information
    buyer_id = Column(Integer, ForeignKey("user.id"))
    buyer_state = Column(Enum(OfferStatesEnum))
    buyer_private_data = Column(JSON)

    # Seller information
    seller_id = Column(Integer, ForeignKey("user.id"))
    seller_state = Column(Enum(OfferStatesEnum))
    seller_private_data = Column(JSON)
