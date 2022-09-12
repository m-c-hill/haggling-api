from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

import enum

from sqlalchemy import JSON, Column, Float, ForeignKey, Integer, String
from sqlalchemy.types import Enum

from ..database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    action_offers = relationship("Offer", foreign_keys='Offer.action_id', lazy=True)
    buyer_offers = relationship("Offer", foreign_keys='Offer.buyer_id', lazy=True)
    seller_offers = relationship("Offer", foreign_keys='Offer.seller_id', lazy=True)
