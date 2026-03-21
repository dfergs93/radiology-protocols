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


def test_load_protocol_path_traversal_blocked():
    response = client.get("/api/protocols/../../backend/app.py")
    assert response.status_code == 403


def test_load_protocol_not_found():
    response = client.get("/api/protocols/ct/cardiac/nonexistent-protocol.md")
    assert response.status_code == 404


def test_load_protocol_returns_structured_data():
    # Use a known protocol that exists in the index
    from app import PROTOCOL_INDEX
    if not PROTOCOL_INDEX:
        pytest.skip("No protocols in index")
    filepath = PROTOCOL_INDEX[0]["filepath"]
    response = client.get(f"/api/protocols/{filepath}")
    assert response.status_code == 200
    data = response.json()
    # Required top-level keys
    for key in ["protocol_name", "author", "last_updated", "category", "protocol_type",
                "clinical_indications", "gantt_raw", "series", "kv", "mas"]:
        assert key in data, f"Missing key: {key}"
