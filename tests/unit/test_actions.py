import pytest

from core.models.offer_models import OfferActionEnum, OfferStatesEnum
from utils.actions import check_action_allowed


def test_action_allowed():
    awaiting_acceptance_state = OfferStatesEnum("AwaitingMyAcceptance")
    accept_action = OfferActionEnum("Accept")

    assert check_action_allowed(state=awaiting_acceptance_state, action=accept_action)


def test_action_not_allowed():
    cancelled_state = OfferStatesEnum("Cancelled")
    accept_action = OfferActionEnum("Accept")

    assert not check_action_allowed(state=cancelled_state, action=accept_action)
