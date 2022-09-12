from sqlalchemy.orm import Session

from core.models import user_models
from core.schemas import user_schema


def get_user(db: Session, user_id: int):
    return (
        db.query(user_models.User).filter(user_models.User.id == user_id).one_or_none()
    )


def get_user_by_username(db: Session, username: str):
    return (
        db.query(user_models.User).filter(user_models.User.username == username).first()
    )


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    db_user = user_models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
