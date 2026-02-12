import pytest
from fastapi.testclient import TestClient
from app import app 

client = TestClient(app)

def test_health_check():
    """Verify the health check endpoint returns a 200 status and correct status message."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"  # Check only the specific key
    assert "openai_api_key_configured" in data  # Ensure this key exists too

def test_root_page():
    """Ensure the UI index page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Log Analyzer" in response.text

def test_analyze_endpoint_no_file():
    """Verify that calling analyze without a file returns an error."""
    response = client.post("/analyze")
    assert response.status_code == 422  # Unprocessable Entity