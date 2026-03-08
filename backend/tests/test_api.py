import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Test health check endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "JobPilot Backend"}

def test_mcp_status():
    """Test MCP status endpoint."""
    response = client.get("/mcp/status")
    assert response.status_code == 200
    assert response.json() == {"status": "running", "active_agents": 0}

@patch("app.automation.router.LinkedInPlatform")
def test_search_endpoint(mock_linkedin):
    """Test search endpoint with mocked platform."""
    # Setup mock
    mock_instance = AsyncMock()
    mock_linkedin.return_value = mock_instance
    
    mock_instance.search_jobs.return_value = [
        {"title": "Dev", "company": "Test Co", "url": "http://test.com", "platform": "LinkedIn"}
    ]
    
    response = client.post("/api/automation/search", json={
        "platform": "linkedin",
        "query": "python",
        "location": "remote"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Dev"
    
    mock_instance.search_jobs.assert_called_once_with("python", "remote")

@patch("app.automation.router.IndeedPlatform")
def test_apply_endpoint_dry_run(mock_indeed):
    """Test apply endpoint dry run."""
    # Setup mock
    mock_instance = AsyncMock()
    mock_indeed.return_value = mock_instance
    
    # We don't need to mock apply_to_job return value because it runs in background task
    # But we can verify the response immediately
    
    response = client.post("/api/automation/apply", json={
        "platform": "indeed",
        "job_url": "http://indeed.com/viewjob",
        "resume_path": "/tmp/resume.pdf",
        "dry_run": True
    })
    
    assert response.status_code == 200
    assert response.json()["status"] == "Application process started"
    assert response.json()["dry_run"] is True

def test_invalid_platform_search():
    """Test search with invalid platform."""
    response = client.post("/api/automation/search", json={
        "platform": "unknown",
        "query": "python",
        "location": "remote"
    })
    
    assert response.status_code == 400
    assert "Unsupported platform" in response.json()["detail"]
