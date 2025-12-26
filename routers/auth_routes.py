# routers/auth_routes.py
from datetime import timedelta

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=["auth"])


# 🔑 Aquí defines las "credenciales" válidas para pedir token
VALID_CLIENT_ID = "math-api-client"
VALID_CLIENT_SECRET = "super-secret-123"   # cámbialo y guárdalo bien


class TokenRequest(BaseModel):
    client_id: str
    client_secret: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/auth/token", response_model=TokenResponse)
async def generate_token(body: TokenRequest):
    """
    Genera un JWT si las credenciales son correctas.
    """
    if body.client_id != VALID_CLIENT_ID or body.client_secret != VALID_CLIENT_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
        )

    # claims que quieras dentro del token
    token_data = {
        "sub": body.client_id,
        "access": "m",
    }

    access_token = create_access_token(
        data=token_data,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return TokenResponse(access_token=access_token)
