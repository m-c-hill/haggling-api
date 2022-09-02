from models.database import Offer, Action


# Turn this into a wrapper?
def action_validator(offer: Offer, action: Action) -> bool:
    """
    Given the state of an offer, validate that a specific action may be taken
    """
    pass