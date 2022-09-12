from enum import Enum
from typing import Union

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core.database import get_db
from core.schemas import error_schema, offer_schema, user_schema
from utils import crud_users

user_router = APIRouter(tags=["users"])


@user_router.get(
    "/users/{user_id}",
    response_model=user_schema.UserResponse,
    responses={404: {"model": error_schema.Response404}},
    tags=["users"],
)
async def get_user_by_id(
    user_id: int = Path(title="The ID of the User"),
    db: Session = Depends(get_db),
):
    """
    Get a single user by id, display their public information.
    """
    user = crud_users.get_user(db, user_id=user_id)

    if not user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=error_schema.Response404(message="test"),
        )
    return user_schema.UserResponse(success=True, user=user)


@user_router.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.UserResponse,
    tags=["users"],
)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user by submitted a unique username that has not been previously
    registered.
    """
    db_user = crud_users.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Username {db_user.username} already registered",
        )
    new_user = crud_users.create_user(db=db, user=user)
    return user_schema.UserResponse(success=True, user=new_user)


@user_router.get("/users/{id}/offers", tags=["users"])
def get_user_offers(
    id: int = Path(title="The ID of the User"),
    active: Union[bool, None] = Query(default=None),
):
    """
    Retrieve offers a user is involved in.
    """
    # TODO
    return
