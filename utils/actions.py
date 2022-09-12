from core.models.offer_models import Offer, OfferActionEnum, OfferStatesEnum

state_action_matrix = {
    "AwaitingMyAcceptance": ("Accept", "ProposeUpdate", "Cancel", "UpdatePrivateData"),
    "AwaitingTheirAcceptance": ("Withdraw", "Cancel", "UpdatePrivateData"),
    "WithdrawnByMe": ("ProposeUpdate", "Cancel", "UpdatePrivateData"),
    "WithdrawnByThem": ("Cancel", "UpdatePrivateData"),
    "Accepted": ("UpdatePrivateData"),
    "Cancelled": ("UpdatePrivateData"),
}


def check_action_allowed(state: OfferStatesEnum, action: OfferActionEnum) -> bool:
    """
    Given the current state of an offer, check that a specific action may be taken
    by a user.
    """
    return action.value in state_action_matrix[state.value]
