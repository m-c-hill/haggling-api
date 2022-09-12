from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
