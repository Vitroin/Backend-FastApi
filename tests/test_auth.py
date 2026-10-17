import pytest
from pydantic import ValidationError

from app.config import Settings
from app.main import app

PUBLIC_PATHS = {"/"}

# Every route not listed in PUBLIC_PATHS must require the service token,
# so a new endpoint added without auth makes these tests fail.
PROTECTED_ROUTES = [
    (method.upper(), path)
    for path, operations in app.openapi()["paths"].items()
    if path not in PUBLIC_PATHS
    for method in operations
]
assert PROTECTED_ROUTES, "no routes discovered"

BAD_HEADERS = {
    "missing": {},
    "wrong": {"X-Service-Token": "wrong-token"},
    "non-ascii": {"X-Service-Token": "tok\xe9n".encode("latin-1")},
}


@pytest.mark.parametrize(("method", "path"), PROTECTED_ROUTES)
@pytest.mark.parametrize("headers", BAD_HEADERS.values(), ids=BAD_HEADERS.keys())
def test_protected_routes_reject_bad_token(client, method, path, headers):
    response = client.request(method, path, headers=headers)
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized Service"}


@pytest.mark.parametrize(("method", "path"), PROTECTED_ROUTES)
def test_protected_routes_accept_valid_token(client, auth_headers, method, path):
    # Routes that need a body may still return 422; this only checks auth passed
    assert client.request(method, path, headers=auth_headers).status_code != 401


def test_root_is_public(client):
    assert client.get("/").status_code == 200


def test_settings_reject_short_token(monkeypatch):
    monkeypatch.setenv("SERVICE_TOKEN", "too-short")
    with pytest.raises(ValidationError):
        Settings()
