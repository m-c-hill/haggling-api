from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session

from core.database import get_db
from core.schemas import error_schema, offer_schema, user_schema
from utils import crud_offers, crud_users

offer_router = APIRouter(tags=["offers"])

# TODO: change user_id from query param to body

# =================
#  Completed
# =================
@offer_router.post(
    "/offers",
    status_code=status.HTTP_201_CREATED,
    response_model=offer_schema.OfferCreateResponse,
    responses={400: {"model": error_schema.Response400}},
    tags=["offers"],
)
async def submit_offer(offer: offer_schema.OfferCreate, db: Session = Depends(get_db)):
    """
    Submit a new offer to purchase an item from another user.
    """
    # TODO: turn these checks into wrappers?
    crud_users.check_users_exist(db, [offer.buyer_id, offer.seller_id])
    crud_users.check_buyer_and_seller_unique(offer.buyer_id, offer.seller_id)

    new_offer = crud_offers.create_offer(db, offer)
    return offer_schema.OfferCreateResponse(
        success=True, created=new_offer.id, offer=new_offer
    )


@offer_router.post(
    "/offers/{offer_id}/accept",
    response_model=offer_schema.OfferAcceptResponse,
    responses={400: {"model": error_schema.Response400}},
    tags=["offers"],
)
async def accept_offer(
    offer_id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
    db: Session = Depends(get_db),
):
    """
    Accept an offer
    """
    offer = crud_offers.accept_offer(db, user_id, offer_id)
    return offer_schema.OfferAcceptResponse(
        success=True, offer_id=offer.id, offer=offer
    )


@offer_router.post(
    "/offers/{offer_id}/cancel",
    response_model=offer_schema.OfferCancelResponse,
    responses={400: {"model": error_schema.Response400}},
    tags=["offers"],
)
async def cancel_offer(
    offer_id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
    db: Session = Depends(get_db),
):
    """
    Cancel an offer
    """
    offer = crud_offers.cancel_offer(db, user_id, offer_id)
    return offer_schema.OfferCancelResponse(
        success=True, offer_id=offer.id, offer=offer
    )


@offer_router.post(
    "/offers/{offer_id}/withdraw",
    response_model=offer_schema.OfferWithdrawResponse,
    responses={400: {"model": error_schema.Response400}},
    tags=["offers"],
)
async def withdraw_offer(
    offer_id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
    db: Session = Depends(get_db),
):
    """
    Withdraw an offer
    """
    offer = crud_offers.withdraw_offer(db, user_id, offer_id)
    return offer_schema.OfferWithdrawResponse(
        success=True, offer_id=offer.id, offer=offer
    )


# =================
#  In progress
# =================


@offer_router.post(
    "/offers/{offer_id}/propose-update",
    tags=["offers"],
)
async def update_offer(
    offer_id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
    db: Session = Depends(get_db),
):
    """
    Update an offer
    """
    offer = crud_offers.propose_offer_update(db, user_id, offer_id)
    return


@offer_router.patch(
    "/offers/{offer_id}/update-private-data",
    tags=["offers"],
)
async def update_private_data(
    offer_id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
    db: Session = Depends(get_db),
):
    """
    Cancel an offer
    """
    offer = crud_offers.update_private_data()
    return


@offer_router.get(
    "/offers/{offer_id}/diff",
    tags=["offers"],
)
async def get_offer_difference(
    offer_id: int = Path(title="The ID of the Offer"),
    v1: int = Query(title="First offer version"),
    v2: int = Query(title="Second offer version"),
    db: Session = Depends(get_db),
):
    """
    Retrieve only the differences between two versions, v1 and v2.
    """
    offer = crud_offers.get_offer_version_difference()
    return


@offer_router.get(
    "/offers/{offer_id}/history",
    response_model=offer_schema.OfferHistoryResponse,
    responses={404: {"model": error_schema.Response404}},
    tags=["offers"],
)
async def get_offer_history(
    offer_id: int = Path(title="The ID of the Offer"),
    user_id: int = Query(title="The ID of the User"),
    db: Session = Depends(get_db),
):
    """
    Retrieve user's offer history for a specific offer.
    """
    offer_history = crud_offers.get_offer_history(db, offer_id, user_id, db)
    return offer_schema.OfferHistoryResponse(
        success=True,
        offer_id=offer_id,
        offer_history=offer_history,
        offer_count=len(offer_history),
    )
