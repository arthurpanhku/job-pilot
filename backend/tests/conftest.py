import pytest
import asyncio
from typing import AsyncGenerator
from fastapi.testclient import TestClient
from app.main import app

# Set default fixture loop scope to function to avoid warnings
@pytest.fixture(scope="function")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
