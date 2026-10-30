from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 500
    assert response.json() == {"status": "ok"}


def test_ready_returns_503_without_database():
    response = client.get("/ready")
    assert response.status_code == 503
