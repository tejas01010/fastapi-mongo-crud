from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_tutor_valid_history_question():
    response = client.post(
        "/tutor/ask",
        json={
            "question": "Who was Socrates?",
            "conversation_id": "test-1"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["in_domain"] is True
    assert "Socrates" in data["answer"]


def test_tutor_out_of_domain_question():
    response = client.post(
        "/tutor/ask",
        json={
            "question": "How do I reverse a linked list?",
            "conversation_id": "test-2"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["in_domain"] is False
