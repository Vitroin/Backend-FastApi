# Contains reusable functions for things like authentication, database sessions, or retrieving
# the current user. Similar to reusable providers and guards in NestJS, although the mechanisms differ.
# Provides authentication or a database session

import secrets
from typing import Annotated

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

from .config import settings

# Registers the header as a security scheme, so /docs shows an "Authorize" button
service_token_header = APIKeyHeader(name="X-Service-Token", auto_error=False)


def verify_service_token(
    x_service_token: Annotated[str | None, Security(service_token_header)],
):
    expected = settings.service_token.get_secret_value()
    # Compare as bytes: compare_digest raises TypeError on non-ASCII strings
    if x_service_token is None or not secrets.compare_digest(
        x_service_token.encode(), expected.encode()
    ):
        raise HTTPException(status_code=401, detail="Unauthorized Service")
