from sqlalchemy.orm import Session

from core.models import offer_models
from core.schemas import offer_schema


def get_offer(db: Session, offer_id: int):
    return (
        db.query(offer_models.Offer).filter(offer_models.Offer.id == offer_id).one_or_none()
    )


def create_offer(db: Session, offer: offer_schema.OfferCreate):
    db_offer = offer_models.Offer(
        offer_id = get_new_offer_id(db),
        version_id = 1,
        product = offer.product,
        quantity = offer.quantity,
        price = offer.price,
        action_id = offer.buyer_id,
        action = offer_models.OfferActionEnum("Submit"),
        buyer_id = offer.buyer_id,
        buyer_state = offer_models.OfferStatesEnum("AwaitingTheirAcceptance"),
        buyer_private_data = offer.buyer_private_data,
        seller_id = offer.seller_id,
        seller_state = offer_models.OfferStatesEnum("AwaitingMyAcceptance"),
        seller_private_data = {}
    )
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer


def get_offer_history():
    return


def get_offers_for_user(db: Session, skip: int = 0, limit: int = 100):
    return


def get_active_offers_for_user():
    return


def action_offer():
    return


# TODO
def get_new_offer_id(db: Session):
    return 1
