from sqlalchemy.orm import Session

from core.models import offer_models
from core.schemas import offer_schema


def get_offer(db: Session, offer_id: int):
    return (
        db.query(offer_models.Offer).filter(offer_models.Offer.id == offer_id).one_or_none()
    )


def get_offer_history():
    return


def get_offers_for_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(offer_models.Offer).offset(skip).limit(limit).all()


def get_active_offers_for_user():
    return

def create_offer(db: Session, user: offer_schema.OfferCreate):
    db_user = offer_models.Offer(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def action_offer():
    return
