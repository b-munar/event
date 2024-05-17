import pytest
import json
from unittest.mock import patch
from functools import wraps

def mock_authorization(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            kwargs["user"] = {"id" : "29a3ad78-6d3c-46e3-9c42-857ca3ec5220"}
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

def test_request_post_register(client):
    url = "/event/sportmen"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "event_id": "3ebb7955-7c2b-479f-8d8f-1fb02700b5b7"
    }
    response2 = client.post(url, data=json.dumps(data), headers=headers)
    assert response2.status_code == 201
    
    
def test_request_delete_sportmen(client):
    url2 = "/event/sportmen"
    headers = {
        "Content-Type": "application/json"
    }
    data2 = {
    "event_id": "3ebb7955-7c2b-479f-8d8f-1fb02700b5b7"
    }
    response = client.delete(url2, data=json.dumps(data2), headers=headers)
    assert response.status_code == 200
