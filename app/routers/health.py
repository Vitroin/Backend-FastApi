from fastapi import APIRouter, Depends

from ..dependencies import verify_service_token

router = APIRouter(
    prefix="/health",
    tags=["Health"],
    dependencies=[Depends(verify_service_token)],
)


@router.post("/health-check")
async def health_check():
    return {
        "success": True,
        "message": "NestJS successfully called FastAPI!",
    }
