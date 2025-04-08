import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app
from fastapi.testclient import TestClient

# Create a new database engine for testing
TEST_DATABASE_URL = "sqlite:///./test_integration.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency override for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="function")
def test_customer(test_client):
    # Create a test customer
    customer_data = {"name": "Test User", "email": "test.user@example.com"}
    response = test_client.post("/customer/edit", data=customer_data)
    assert response.status_code == 200
    return response.json()

def test_get_customer_edit(test_client, test_customer):
    customer_id = test_customer['id']
    response = test_client.get(f"/customer/edit/{customer_id}")
    assert response.status_code == 200
    assert response.json()['name'] == "Test User"
    assert response.json()['email'] == "test.user@example.com"

def test_post_customer_edit(test_client, test_customer):
    customer_id = test_customer['id']
    update_data = {"name": "Updated User", "email": "updated.user@example.com"}
    response = test_client.post(f"/customer/edit/{customer_id}", data=update_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Customer Updated User with email updated.user@example.com updated successfully!"}

    # Verify the update in the database
    response = test_client.get(f"/customer/edit/{customer_id}")
    assert response.status_code == 200
    assert response.json()['name'] == "Updated User"
    assert response.json()['email'] == "updated.user@example.com"
