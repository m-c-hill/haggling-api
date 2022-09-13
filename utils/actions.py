from fastapi import HTTPException, status

from core.models.offer_models import Offer, OfferActionEnum, OfferStatesEnum

state_action_matrix = {
    "AwaitingMyAcceptance": ("Accept", "ProposeUpdate", "Cancel", "UpdatePrivateData"),
    "AwaitingTheirAcceptance": ("Withdraw", "Cancel", "UpdatePrivateData"),
    "WithdrawnByMe": ("ProposeUpdate", "Cancel", "UpdatePrivateData"),
    "WithdrawnByThem": ("Cancel", "UpdatePrivateData"),
    "Accepted": ("UpdatePrivateData"),
    "Cancelled": ("UpdatePrivateData"),
}


def check_action_allowed(offer: Offer, action: OfferActionEnum, user_id: int) -> None:
    """
    Given the current state of an offer, check that a specific action may be taken
    by a user.
    """
    state = get_user_offer_state(offer, user_id)

    if action.value not in state_action_matrix[state.value]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User {user_id} cannot perform `{action.value}` when offer is in state `{state.value}`",
        )


def get_user_offer_state(offer: Offer, user_id: int) -> OfferStatesEnum:
    """
    Retrieve the state of the offer relative to the current user
    """
    return offer.buyer_state if offer.buyer_id == user_id else offer.seller_state
