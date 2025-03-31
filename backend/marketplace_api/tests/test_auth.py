import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

@pytest.fixture
def test_user():
    return {"email": "test@example.com", "password": "1234", "full_name": "Test User"}

def test_signup(test_user):
    response = client.post("/auth/signup", json=test_user)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["email"] == test_user["email"]
