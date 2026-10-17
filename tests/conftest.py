import os

# Set before the app is imported; real env vars take priority over .env
os.environ["SERVICE_TOKEN"] = "test-service-token-0123456789abcdef"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from app.main import app  # noqa: E402


@pytest.fixture
def client():
    # The context manager runs the lifespan (MongoDB client startup/shutdown)
    with TestClient(app) as client:
        yield client


@pytest.fixture
def auth_headers():
    return {"X-Service-Token": os.environ["SERVICE_TOKEN"]}
