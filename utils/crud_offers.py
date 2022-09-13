from sqlalchemy.orm import Session

from core.models import offer_models
from core.schemas import offer_schema
from utils.actions import check_action_allowed


# TODO
def get_new_offer_id(db: Session):
    return 1


# =================
#  Completed
# =================


def create_offer(db: Session, offer: offer_schema.OfferCreate) -> offer_models.Offer:
    db_offer = offer_models.Offer(
        offer_id=get_new_offer_id(db),
        version_id=1,
        product=offer.product,
        quantity=offer.quantity,
        price=offer.price,
        action_id=offer.buyer_id,
        action=offer_models.OfferActionEnum("Submit"),
        buyer_id=offer.buyer_id,
        buyer_state=offer_models.OfferStatesEnum("AwaitingTheirAcceptance"),
        buyer_private_data=offer.buyer_private_data,
        seller_id=offer.seller_id,
        seller_state=offer_models.OfferStatesEnum("AwaitingMyAcceptance"),
        seller_private_data={},
    )
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer


def accept_offer(db: Session, user_id: int, offer_id: int) -> offer_models.Offer:
    offer_item = get_latest_offer_item(db, offer_id)
    check_action_allowed(offer_item, offer_models.OfferActionEnum("Accept"), user_id)

    db_offer = offer_models.Offer(
        offer_id=offer_item.offer_id,
        version_id=offer_item.version_id + 1,
        product=offer_item.product,
        quantity=offer_item.quantity,
        price=offer_item.price,
        action_id=user_id,
        action=offer_models.OfferActionEnum("Accept"),
        buyer_id=offer_item.buyer_id,
        buyer_state=offer_models.OfferStatesEnum("Accepted"),
        buyer_private_data=offer_item.buyer_private_data,
        seller_id=offer_item.seller_id,
        seller_state=offer_models.OfferStatesEnum("Accepted"),
        seller_private_data=offer_item.seller_private_data,
    )
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer


def cancel_offer(db: Session, user_id: int, offer_id: int) -> offer_models.Offer:
    offer_item = get_latest_offer_item(db, offer_id)
    check_action_allowed(offer_item, offer_models.OfferActionEnum("Accept"), user_id)

    db_offer = offer_models.Offer(
        offer_id=offer_item.offer_id,
        version_id=offer_item.version_id + 1,
        product=offer_item.product,
        quantity=offer_item.quantity,
        price=offer_item.price,
        action_id=user_id,
        action=offer_models.OfferActionEnum("Cancel"),
        buyer_id=offer_item.buyer_id,
        buyer_state=offer_models.OfferStatesEnum("Cancelled"),
        buyer_private_data=offer_item.buyer_private_data,
        seller_id=offer_item.seller_id,
        seller_state=offer_models.OfferStatesEnum("Cancelled"),
        seller_private_data=offer_item.seller_private_data,
    )
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer


def withdraw_offer(db: Session, user_id: int, offer_id: int) -> offer_models.Offer:
    offer_item = get_latest_offer_item(db, offer_id)
    check_action_allowed(offer_item, offer_models.OfferActionEnum("Accept"), user_id)

    buyer_state = (
        offer_models.OfferStatesEnum("WithdrawnByMe")
        if user_id == offer_item.buyer_id
        else offer_models.OfferStatesEnum("WithdrawnByThem")
    )
    seller_state = (
        offer_models.OfferStatesEnum("WithdrawnByMe")
        if user_id == offer_item.seller_id
        else offer_models.OfferStatesEnum("WithdrawnByThem")
    )

    db_offer = offer_models.Offer(
        offer_id=offer_item.offer_id,
        version_id=offer_item.version_id + 1,
        product=offer_item.product,
        quantity=offer_item.quantity,
        price=offer_item.price,
        action_id=user_id,
        action=offer_models.OfferActionEnum("Withdraw"),
        buyer_id=offer_item.buyer_id,
        buyer_state=buyer_state,
        buyer_private_data=offer_item.buyer_private_data,
        seller_id=offer_item.seller_id,
        seller_state=seller_state,
        seller_private_data=offer_item.seller_private_data,
    )
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer


# =================
#  In progress
# =================


def get_offer_history():
    return


def get_offers_for_user(db: Session, skip: int = 0, limit: int = 100):
    return


def get_active_offers_for_user():
    return


def get_offer_item(db: Session, item_id: int):
    return (
        db.query(offer_models.Offer)
        .filter(offer_models.Offer.id == item_id)
        .one_or_none()
    )


def get_latest_offer_item(db: Session, offer_id: int):
    return (
        db.query(offer_models.Offer)
        .filter(offer_models.Offer.offer_id == offer_id)
        .order_by(offer_models.Offer.version_id.desc())
        .first()
    )
