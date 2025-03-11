from fastapi import FastAPI

from app.models import users as models
from app.database import engine
from app.routers import users

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
