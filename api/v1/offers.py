from fastapi import APIRouter, Path, Query, status, Depends, HTTPException

from core.database import get_db
from core.schemas import error_schema, offer_schema, user_schema
from sqlalchemy.orm import Session

from utils import crud_offers, crud_users

offer_router = APIRouter(tags=["offers"])


@offer_router.post(
    "/offers",
    status_code=status.HTTP_201_CREATED,
    #response_model=offer_schema.OfferResponse,
    responses={404: {"model": error_schema.Response404}},
    tags=["offers"],
)
def submit_offer(offer: offer_schema.OfferCreate, db: Session = Depends(get_db)):
    """
    Submit a new offer to purchase an item from another user.
    """
    
    # TODO: check user cannot submit offer to themselves

    crud_users.check_users_exist(db, [offer.buyer_id, offer.seller_id])

    return "SUCCESS!"


@offer_router.get("/offers/{id}/history")
def get_offer_history(
    id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
):
    """
    Retrieve offer history.
    """
    return


@offer_router.patch("/offers/{id}/accept")
def accept_offer(
    id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
):
    return


@offer_router.patch("/offers/{id}/propose-update")
def update_offer(
    id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
):
    """
    Update an offer
    """
    return


@offer_router.patch("/offers/{id}/withdraw")
def withdraw_offer(
    id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
):
    """
    Withdraw an offer
    """
    return


@offer_router.patch("/offers/{id}/cancel")
def cancel_offer(
    id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
):
    """
    Cancel an offer
    """
    return


@offer_router.get("/offers/{id}/diff")
def get_offer_difference(
    v1: int = Query(title="First offer version"),
    v2: int = Query(title="Second offer version"),
):
    """
    Retrieve only the differences between two versions, v1 and v2.
    """
    return
