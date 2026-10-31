import pytest
from app import app

@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == (
        "Hello from Python, Harness CI and Docker Hub!"
    )

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_info(client):
    response = client.get("/info")
    assert response.status_code == 200
    assert response.get_json()["application"] == "python-harness-ci-demo"

def test_not_found(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404
