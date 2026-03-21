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


def test_generate_missing_protocol_name_returns_422():
    response = client.post("/api/protocols/generate", json={})
    assert response.status_code == 422


def test_generate_invalid_category_returns_422():
    response = client.post("/api/protocols/generate", json={
        "protocol_name": "Test Protocol",
        "author": "Test",
        "last_updated": "2026-03-19",
        "category": "InvalidCategory",
        "protocol_type": "CT",
        "clinical_indications": "Test indication",
        "acquisition_summary": [],
        "patient_positioning": "Supine",
        "npo_status": "None",
        "premedication": "",
        "contrast_agent": "Isovue 370",
        "contrast_volume": "80 mL",
        "contrast_flow_rate": "4 mL/s",
        "contrast_timing_method": "Bolus Tracking",
        "contrast_roi_placement": "Aorta",
        "contrast_trigger": "150 HU",
        "lab_requirements": "",
        "tech_notes": "",
        "nursing_notes": "",
        "radiologist_notes": "",
        "tips_tricks": "",
        "safety_renal_function": "GFR > 30",
        "safety_allergy": "Screen for iodine allergy",
        "gantt_rows": [],
        "gantt_raw": "",
        "series": [],
        "kv": "120",
        "mas": "Auto",
        "rotation_time": "0.5",
        "pitch": "1.375",
        "post_processing": [],
        "additional_recons": ""
    })
    assert response.status_code == 422


VALID_GENERATE_PAYLOAD = {
    "protocol_name": "Test CTA Chest",
    "author": "Test Author",
    "last_updated": "2026-03-19",
    "category": "Chest",
    "protocol_type": "CTA",
    "clinical_indications": "Pulmonary embolism\nAortic dissection",
    "acquisition_summary": [{"series": "CTA Chest", "phase": "Arterial", "coverage": "Thoracic inlet to diaphragm"}],
    "patient_positioning": "Supine, arms up",
    "npo_status": "None required",
    "premedication": "",
    "contrast_agent": "Isovue 370",
    "contrast_volume": "80 mL",
    "contrast_flow_rate": "4 mL/s",
    "contrast_timing_method": "Bolus Tracking",
    "contrast_roi_placement": "Main pulmonary artery",
    "contrast_trigger": "100 HU",
    "lab_requirements": "GFR if renal history",
    "tech_notes": "Breath hold instructions",
    "nursing_notes": "IV access 20g or larger",
    "radiologist_notes": "Review for PE and aorta",
    "tips_tricks": "Increase flow rate if poor IV access",
    "safety_renal_function": "GFR > 30",
    "safety_allergy": "Screen for iodine allergy",
    "gantt_rows": [
        {"label": "Contrast Injection", "duration_seconds": 20, "type": "contrast", "start": "00:00"},
        {"label": "Saline Chase", "duration_seconds": 8, "type": "saline", "start": "after:contrast_injection"},
        {"label": "CTA Chest", "duration_seconds": 8, "type": "scan", "start": "after:contrast_injection"}
    ],
    "gantt_raw": "",
    "series": [
        {"name": "CTA Chest", "start": "Thoracic inlet", "end": "Diaphragm",
         "delay": "Bolus track 100HU", "thickness": "0.625mm", "notes": ""}
    ],
    "kv": "100",
    "mas": "Auto mA",
    "rotation_time": "0.5",
    "pitch": "1.375",
    "post_processing": [
        {"plane": "Axial", "acquisition": "CTA Chest", "fov": "36cm",
         "thickness_increment": "1.25/1.25", "kernel": "Standard", "ir_strength": "3", "notes": ""}
    ],
    "additional_recons": "Coronal and sagittal MPRs"
}


def test_generate_returns_markdown():
    response = client.post("/api/protocols/generate", json=VALID_GENERATE_PAYLOAD)
    assert response.status_code == 200
    data = response.json()
    assert "markdown" in data
    md = data["markdown"]
    assert "# Test CTA Chest" in md
    assert "Category: Chest" in md
    assert "Protocol Type: CTA" in md


def test_generate_markdown_contains_gantt():
    response = client.post("/api/protocols/generate", json=VALID_GENERATE_PAYLOAD)
    md = response.json()["markdown"]
    assert "gantt" in md
    assert "contrast_injection" in md  # slugified label


def test_generate_markdown_contains_series_table():
    response = client.post("/api/protocols/generate", json=VALID_GENERATE_PAYLOAD)
    md = response.json()["markdown"]
    assert "CTA Chest" in md
    assert "Thoracic inlet" in md


def test_generate_empty_clinical_indications_returns_422():
    payload = {**VALID_GENERATE_PAYLOAD, "clinical_indications": ""}
    response = client.post("/api/protocols/generate", json=payload)
    assert response.status_code == 422


def test_generate_gantt_row_zero_duration_returns_422():
    payload = {**VALID_GENERATE_PAYLOAD, "gantt_rows": [
        {"label": "Contrast", "duration_seconds": 0, "type": "contrast", "start": "00:00"}
    ]}
    response = client.post("/api/protocols/generate", json=payload)
    assert response.status_code == 422


def test_generate_gantt_no_duplicate_section_scan():
    """Multiple scan rows should only produce one 'section Scan' header"""
    payload = {**VALID_GENERATE_PAYLOAD, "gantt_rows": [
        {"label": "Contrast", "duration_seconds": 20, "type": "contrast", "start": "00:00"},
        {"label": "Scan Phase 1", "duration_seconds": 8, "type": "scan", "start": "after:contrast"},
        {"label": "Scan Phase 2", "duration_seconds": 8, "type": "scan", "start": "after:scan_phase_1"},
    ]}
    response = client.post("/api/protocols/generate", json=payload)
    md = response.json()["markdown"]
    assert md.count("section Scan") == 1
