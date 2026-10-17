# Matches the endpoint and handles the request
from fastapi import APIRouter, Depends

from ..dependencies import verify_service_token

router = APIRouter(
    prefix="/coach",
    tags=["coaching-tips"],
    dependencies=[Depends(verify_service_token)],
)


@router.get("/coachingTips")
async def read_coaching_tips():
    return {"success": True, "message": "This is the coaching tips endpoint."}


@router.get("/whatWentWell")
async def read_what_went_well():
    return {"success": True, "message": "This is the what went well endpoint."}


@router.get("/whatToImprove")
async def read_what_to_improve():
    return {"success": True, "message": "This is the what to improve endpoint."}


@router.get("/recommendations")
async def read_recommendations():
    return {"success": True, "message": "This is the recommendations endpoint."}
