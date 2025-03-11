from sqlalchemy import Column, Integer, String, Date, UUID
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    age = Column(Integer, index=True)
    date_of_birth = Column(Date, index=True)
