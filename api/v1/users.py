from enum import Enum

from fastapi import Path, Query, APIRouter

from typing import Union


class Tags(Enum):
    users = "users"
    offers = "offers"


user_router = APIRouter(tags=["users"])


@user_router.get(
    "/users/{id}", response_model="", response_model_exclude="", tags=[Tags.users]
)
def get_user(
    id: int = Path(title="The ID of the User"),
):
    """
    Get a single user by id, display their public information.
    """
    return


@user_router.patch("/users/{id}/private-data", tags=[Tags.users])
def update_user_private_data(
    id: int = Path(title="The ID of the User"),
):
    """
    Update a user's private information.
    """
    return


@user_router.get("/users/{id}/offers", tags=[Tags.users])
def get_user_offers(
    id: int = Path(title="The ID of the User"),
    active: Union[bool, None] = Query(default=None),
):
    """
    Retrieve offers a user is involved in.
    """
    return
