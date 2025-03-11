import logging
import uuid
from typing import Generator

from fastapi import Depends, HTTPException, APIRouter

from app.crud import users as crud
from app.database import Session
from app.schemas import users as schemas

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/users", tags=["Users"])


def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()


@router.post("/create", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate, db: Session = Depends(get_db)
) -> schemas.User:
    logger.info(f"Creating user: {user.first_name}, {user.last_name}")
    return schemas.User.model_validate(crud.create_user(db, user))

@router.get("/", response_model=list[schemas.User])
def get_users(
    skip: int = 0, limit: int = 20, db: Session = Depends(get_db)
) -> list[schemas.User]:
    db_users = crud.get_users(db=db, skip=skip, limit=limit)
    return [schemas.User.model_validate(user) for user in db_users]


@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)) -> schemas.User:
    logger.info(f"Fetching user with ID: {user_id}")
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return schemas.User.model_validate(db_user)


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    user_id: uuid.UUID,
    user_update: schemas.UserCreate,
    db: Session = Depends(get_db),
) -> schemas.User:
    logger.info(f"Updating user with ID: {user_id}")
    db_user = crud.update_user(db=db, user_id=user_id, user=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return schemas.User.model_validate(db_user)


@router.delete("/{user_id}")
def delete_user(user_id: uuid.UUID, db: Session = Depends(get_db)) -> dict[str, str]:
    logger.info(f"Deleting user with ID: {user_id}")
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db=db, user_id=user_id)
    return {"message": "User deleted successfully"}
