import uuid
from typing import Type

from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas import users as schemas
from app.models import users as models


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        id=uuid.uuid4(),
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
        date_of_birth=user.date_of_birth,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: uuid.UUID) -> models.User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 20) -> list[Type[User]]:
    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(
    db: Session, user_id: uuid.UUID, user: schemas.UserCreate
) -> Type[User] | None:
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.age = user.age
        db_user.date_of_birth = user.date_of_birth
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: uuid.UUID) -> None:
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
