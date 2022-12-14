from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from core.models import user_models
from core.schemas import user_schema


def get_user(db: Session, user_id: int):
    return (
        db.query(user_models.User).filter(user_models.User.id == user_id).one_or_none()
    )


def get_user_by_username(db: Session, username: str):
    return (
        db.query(user_models.User)
        .filter(user_models.User.username == username)
        .one_or_none()
    )


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    db_user = user_models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_users_exist(db, users: List[str]) -> None:
    for user_id in users:
        if not get_user(db, user_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with id `{user_id}` does not exist",
            )


def check_buyer_and_seller_unique(seller_id: int, buyer_id: int) -> None:
    if seller_id == buyer_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User cannot submit offer to self, choose a different seller",
        )


def check_user_can_access_offer():
    return


def get_offer_history():
    check_user_can_access_offer()  # db, offer_id, user_id)
    return
