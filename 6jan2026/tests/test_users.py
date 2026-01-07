from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

created_user_id = None


def test_create_user():
    global created_user_id

    response = client.post(
        "/users",
        json={
            "name": "Pytest User",
            "email": "pytest@example.com",
            "age": 24
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert "id" in data

    created_user_id = data["id"]


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_invalid_id():
    response = client.get("/users/invalid_id")
    assert response.status_code == 400


def test_delete_user():
    response = client.delete(f"/users/{created_user_id}")
    assert response.status_code == 200


def test_delete_user_again():
    response = client.delete(f"/users/{created_user_id}")
    assert response.status_code == 404
