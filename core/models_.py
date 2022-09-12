# from __future__ import annotations
# from enum import unique

# from itertools import product
# from typing import List

# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
# from sqlalchemy.orm import relationship

# from .database import Base


# class User(Base):
#     tablename = "__user__"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True)
#     # offers: List[Offer]
#     private_data = Column(JSON)

#     def __init__():
#         pass

#     def update_private_data(self, updates: dict):
#         self.private_data = {**self.private_data, **self.updates}


# class Offer(Base):
#     tablename = "__offer__"

#     id: int
#     offer_id: int
#     version: int  # default == 1
#     product: str
#     quantity: int
#     price: float
#     seller_id: int
#     buyer_id: int
#     state: str

#     def get_offer_history(self):
#         pass
