import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_protocols_list_returns_list():
    response = client.get("/api/protocols")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_protocols_list_entries_have_required_fields():
    response = client.get("/api/protocols")
    assert response.status_code == 200
    data = response.json()
    if data:  # Skip if index is empty
        entry = data[0]
        assert "title" in entry
        assert "filepath" in entry
