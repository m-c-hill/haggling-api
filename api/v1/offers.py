from fastapi import Path, status, Query, APIRouter


offer_router = APIRouter(tags=["offers"])


@offer_router.post(
    "/offers",
    status_code=status.HTTP_201_CREATED,
    summary="",
)
def submit_offer():
    """
    Submit a new offer with the following information:
    - **product**
    - **quantity**
    - **price**
    - **seller_id**
    - **buyer_id**
    """
    return


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
