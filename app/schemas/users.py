import datetime
import uuid

from pydantic import BaseModel


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    date_of_birth: datetime.date


class User(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    age: int
    date_of_birth: datetime.date

    class Config:
        from_attributes = True
