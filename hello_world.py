from enum import Enum


class OfferStatesEnum(Enum):
    awaiting_my_acceptance = "AwaitingMyAcceptance"
    awaiting_their_acceptance = "AwaitingTheirAcceptance"
    withdrawn_by_me = "WithdrawnByMe"
    withdrawn_by_them = "WithdrawnByThem"
    accepted = "Accepted"
    cancelled = "Cancelled"
