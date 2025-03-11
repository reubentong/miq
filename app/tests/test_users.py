import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Session, engine, Base
from app.models.users import User
from datetime import datetime

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = Session()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client():
    client = TestClient(app)
    yield client


def test_create_user(client, db):
    user_data = {
        "first_name": "Test User",
        "last_name": "Test",
        "age": 28,
        "date_of_birth": "1990-01-01",
    }

    response = client.post("/users/create", json=user_data)

    assert response.status_code == 200
    assert response.json()["first_name"] == user_data["first_name"]
    assert response.json()["last_name"] == user_data["last_name"]
    assert response.json()["age"] == user_data["age"]
    assert response.json()["date_of_birth"] == user_data["date_of_birth"]

    db_user = db.query(User).filter(User.last_name == user_data["last_name"]).first()
    assert db_user is not None
    assert db_user.first_name == user_data["first_name"]
    assert db_user.last_name == user_data["last_name"]
    assert db_user.age == user_data["age"]
    assert db_user.date_of_birth == datetime.strptime(user_data["date_of_birth"], '%Y-%m-%d').date()
