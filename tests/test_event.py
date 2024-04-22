import pytest
import json
from unittest.mock import patch
from functools import wraps

def mock_authorization(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            kwargs["user"] = {"id" : "9027aff6-545e-4a1c-bbf7-9c09f6ae595c"}
            return func(*args, **kwargs)
    return decorated

patch('src.utils.authorization.authorization', mock_authorization).start()

from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_request_ping(client):
    response = client.get("/events/ping")
    assert response.status_code == 200
    assert b"pong" in response.data

def test_request_post(client):
    url = "/events"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "titulo": "evente",
    "fecha":"2019-05-05",
    "description":"Test event",
    "hora": "17:00",
    "location":"Mall"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201

def test_request_get(client):
    url = "/events"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "titulo": "evente",
    "fecha":"2019-05-05",
    "description":"Test event",
    "hora": "17:00",
    "location":"Mall"
    }
    client.post(url, data=json.dumps(data), headers=headers)
    response = client.get("/events")
    assert response.status_code == 200
    assert b"events" in response.data